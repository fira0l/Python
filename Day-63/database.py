from flask import Flask
from flask_sqlalchemy import SQLAlchemy

App= Flask(__name__)

App.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
App.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(App)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float(), nullable=False)

    def __repr__(self):
        return '<Title %r>' % self.title
