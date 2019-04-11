from trail import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    books = db.relationship('Book', secondary='reads', backref='readby')

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True, nullable=False)
    # author = db.Column(db.String(120), unique=True, nullable=False)
    ISBN = db.Column(db.String(13))
    authors = db.relationship('Author', secondary='author_books', backref='books')
    # authors = db.relationship('Author', secondary=authors, backref='books', lazy=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))   
    # user = db. relationship('User', secondary='reads', backref='reads')


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

class AuthorBooks(db.Model):
    authorid = db.Column(db.Integer, db.ForeignKey('author.id'), primary_key=True )
    bookid = db.Column(db.Integer, db.ForeignKey('book.id'), primary_key=True )
    author = db.relationship(Author, backref = 'book_assc')
    books = db.relationship(Book, backref = 'author_assc')


class Reads(db.Model):
    bookid = db.Column(db.Integer, db.ForeignKey('book.id'), primary_key=True )
    userid = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True )
    rating = db.Column(db.Integer)
    user =  db.relationship(User, backref = 'books_assc')
    book =  db.relationship(Book, backref = 'users_assc')


# class Tag(db.Model):
#     id = db.Column(db.Integer, primary_key=True)








