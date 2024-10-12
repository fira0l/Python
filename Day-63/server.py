from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from database import db, Book, App
# import sqlite3

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# # cursor.execute(
# #     "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(2, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

app = Flask(__name__)
app.config["SECRET_KEY"] = "Thisismysecretkey"

Bootstrap(app)


all_books = []


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
        with App.app_context():
            new_book = Book(id=1, title=book['title'], author=book["author"], rating=book["rating"])
            db.session.add(new_book)
            db.session.commit()

            books = Book.query.all()

        return render_template('index.html', books=books)

    return render_template('add.html', form=form)


if __name__ == '__main__':
    with App.app_context():
        db.create_all()
    app.run(debug=True)
