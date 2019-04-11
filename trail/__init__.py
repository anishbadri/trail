from flask import Flask
from flask_sqlalchemy import SQLAlchemy 


app=Flask(__name__)

app.config['SECRET_KEY'] = 'cac873583f189291c68823d86860459a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


from trail import routes