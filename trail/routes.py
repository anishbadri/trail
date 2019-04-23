from trail import db, app
from flask import render_template, url_for, flash, redirect, request
from trail.models import User, Book, Author, Reads, AuthorBooks
from trail.forms import RegistrationForm, LoginForm, AddBook, SearchBook
from flask_login import login_user, current_user, logout_user, login_required
import requests
import urllib.parse


class bookDetails:
    def __init__(self, title, author, image):
        self.title = title
        self.author = author 
        self.image = image


class storeBook:
    def __init__(self, title, subtitle, authors, imageLink, isbn, id):
        self.title = title
        self.subtitle = subtitle
        self.authors = authors
        self.imageLink = imageLink
        self.isbn = isbn
        self.googleid = id

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('registration.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()

        if user and user.password == form.password.data:  
            login_user(user)
            next_page = request.args.get('next')

            return redirect(next_page) if next_page else redirect(url_for('home'))

    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/addbook', methods=['GET', 'POST'])
def addbook():
    form = AddBook()

    if form.validate_on_submit():
        user = current_user
        author = Author.query.filter_by(name = form.authors.data).first()
        if author == None:
            author = Author(name = form.authors.data)
        book = Book(title = form.title.data, ISBN = form.ISBN.data, authors = [author])
        reads = Reads(user = user, book = book, rating = form.rating.data)
        db.session.add(reads)
        db.session.commit()
    
    return render_template('addbook.html', form=form)

@app.route('/book/<int:book_id>', methods=['GET', 'POST'])
def book(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('book.html', book = book)



@app.route('/searchbook', methods=['GET', 'POST'])
@login_required
def searchbook():
    form = SearchBook()  
    if form.validate_on_submit():
        search = form.title.data
        constlink = 'https://www.googleapis.com/books/v1/volumes?'
        link = constlink + urllib.parse.urlencode({'q': search})
        
        newstr = requests.get(link).json()
        print(type(newstr['items']))
        title = newstr['items'][0]['volumeInfo']['title']
        authors = ", ".join(newstr['items'][0]['volumeInfo']['authors'])
        image = newstr['items'][0]['volumeInfo']['imageLinks']['smallThumbnail']
        searchedBook = bookDetails(title,authors, image)
        isbn = newstr['items'][0]['id']
        return render_template('searchbook.html', form = form, data=searchedBook, isbn = isbn)
    return render_template('searchbook.html', form = form, data=None, )

@app.route('/displaybook/<book>')
def displayBook(book):
    print(book.title)
    return render_template('displayBook.html', book=book)

@app.route('/addnewBook/<data>')
@login_required
def addnewBook(data):
    link = 'https://www.googleapis.com/books/v1/volumes/' + data
    jsondata = requests.get(link).json()
    newbook=getBookData(jsondata)
    bookAuthor = Author
    book = Book(title=newbook.title, subtitle=newbook.subtitle, imageLink = newbook.imageLink, googleid = newbook.googleid, isbn=newbook.isbn)
    for author in newbook.authors:
        bookAuthor = Author(name = author)
        db.session.add(AuthorBooks(author=bookAuthor, books = book))
    userbook = Reads(user = current_user, book = book)
    db.session.add(userbook)
    db.session.commit()

    dbbook = Book.query.filter_by(title = newbook.title).first()
    
    return render_template('displayBook.html',  book=dbbook, user = current_user)

def getBookData(data):
    title = data['volumeInfo']['title']
    subtitle = data['volumeInfo']['subtitle']
    isbn = data['volumeInfo']['industryIdentifiers'][1]['identifier']
    image = data['volumeInfo']['imageLinks']['smallThumbnail']
    authors = data['volumeInfo']['authors']
    googleid = data['id']
    newBook = storeBook(title,subtitle,authors,image,isbn, googleid)

    return newBook

    # image = data['items'][]
    # image = 
    # book = displayBook()

@app.route('/<int:userid>/books')
@login_required
def displayuserbook(userid):
    user = User.query.filter_by(id = userid).first()
    return render_template('displayUserBooks.html', user = user)
