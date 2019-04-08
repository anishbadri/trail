# from trail import db


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(60), nullable=False)

#     # def __repr__(self):
    #     return f"User('{self.username}', '{self.email}')"



# tags = db.Table('tags',
#     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
#     db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True)
# )

# class Book(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(20), unique=True, nullable=False)
#     author = db.Column(db.String(120), unique=True, nullable=False)
#     ISBN = db.Column(db.String(13), nullable=False)
#     tags = db.relationship('Tag', secondary=tags, backref='books', lazy=True)


# class Tag(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(40), unique=True, nullable=False)



