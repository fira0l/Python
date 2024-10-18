from flask_sqlalchemy import SQLAlchemy
from flask import Flask

App = Flask(__name__)


App.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
App.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(App)


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return 'Title <%r>' % self.title

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary
