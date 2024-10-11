from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy


# import sqlite3

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# # cursor.execute(
# #     "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(2, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

app = Flask(__name__)
app.config["SECRET_KEY"] = "Thisismysecretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Bootstrap(app)

all_books = []


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float(), nullable=False)

    def __repr__(self):
        return '<Title %r>' % self.title


db.create_all()

class BookSubmissionForm(FlaskForm):
    name = StringField("Title", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    rating = StringField("Rating")
    submit = SubmitField("Submit")


@app.route('/')
def home():
    return render_template('index.html', books=all_books)


@app.route('/add', methods=["GET", "POST"])
def add():
    form = BookSubmissionForm()
    if form.validate_on_submit():
        book = {
            "title": form.name.data,
            "author": form.author.data,
            "rating": form.rating.data,
        }
        all_books.append(book)
        return render_template('index.html', books=all_books)

    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
