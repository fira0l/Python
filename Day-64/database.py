from flask import Flask
from flask_sqlalchemy import SQLAlchemy

App = Flask(__name__)


App.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie_database.db"
App.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(App)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    rating = db.Column(db.Float(), nullable=False)
    ranking = db.Column(db.Integer(), nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return 'Title <%r>' % self.title
