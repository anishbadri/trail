from flask import Flask
from flask_sqlalchemy import SQLAlchemy 


app=Flask(__name__)

app.config['SECRET_KEY'] = 'cac873583f189291c68823d86860459a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# tags = db.Table('tags',
#     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
#     db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True)
# )

# authors = db.Table('author',
#     db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True),
#     db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True)
# )

# ratings = db.Table('ratings',
#     db.Column('user_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
#     db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True)
# )

# class Book(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(20), unique=True, nullable=False)
#     author = db.Column(db.String(120), unique=True, nullable=False)
#     ISBN = db.Column(db.String(13), nullable=False)
#     authors = db.relationship('Author', secondary=authors, backref='books', lazy=True)
#     tags = db.relationship('Tag', secondary=tags, backref='books', lazy=True)


# class Tag(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(40), unique=True, nullable=False)



# # class Author(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     name = db.Column(db.String(60), unique=True, nullable=False)

# class ReadRating(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     rating = db.Column(db.Integer, unique=True, nullable=False)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True, nullable=False)
    # author = db.Column(db.String(120), unique=True, nullable=False)
    # ISBN = db.Column(db.String(13), nullable=False)
    # authors = db.relationship('Author', secondary=authors, backref='books', lazy=True)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))   exit
    user = db. relationship('User', secondary='reads', backref='reads')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    # books = db.relationship('Book', secondary='reads')exi

class Reads(db.Model):
    bookid = db.Column(db.Integer, db.ForeignKey('book.id'), primary_key=True )
    userid = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True )
#     rating = db.Column(db.Integer)
#     user =  db.relationship(User, backref = 'books_assc')
#     book =  db.relationship(Book, backref = 'users_assc')
