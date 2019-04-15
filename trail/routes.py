from trail import db, app
from flask import render_template, url_for, flash, redirect, request
from trail.models import User, Book, Author, Reads
from trail.forms import RegistrationForm, LoginForm, AddBook
from flask_login import login_user, current_user, logout_user, login_required



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




