from flask_sqlalchemy import SQLAlchemy
from flask import Flask


App = Flask(__name__)

App.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
App.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(App)


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def __repr__(self):
        return 'Name <%r>' % self.name

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary
