from flask import Flask
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

App = Flask(__name__)

# CONNECT TO DB

App.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
App.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(App)

login_manager = LoginManager()
login_manager.init_app(App)


@login_manager.user_loader
def load_user(user):
    with App.app_context():
        return User.query.get(user)


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    posts = relationship("BlogPost", back_populates="author")
    # children = relationship("BlogPost")


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    # Create Foreign Key, "users.id" the users refers to the tablename of User.
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    # Create reference to the User object, the "posts" refers to the posts protperty in the User class.
    author = relationship("User", back_populates="posts")
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    # user_id = db.Column(db.Integer, ForeignKey("User.id"))
    # parent = relationship("User")

    def __repr__(self):
        return 'Title <%r>' % self.title

