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


class EditRatingForm(FlaskForm):
    rating = StringField("Rating")
    submit = SubmitField("Submit")


@app.route('/')
def home():
    with App.app_context():
        books = Book.query.all()
    return render_template('index.html', books=books)


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
            new_book = Book(title=book['title'], author=book["author"], rating=book["rating"])
            db.session.add(new_book)
            db.session.commit()

            books = Book.query.all()

        return render_template('index.html', books=books)

    return render_template('add.html', form=form)


@app.route('/edit/<int:book_id>',methods=["GET", "POST"])
def edit(book_id):
    edit_form = EditRatingForm()

    with App.app_context():
        books = Book.query.all()
        book = Book.query.filter_by(id=book_id).first()
        book_to_update_by_filter = Book.query.filter_by(id=book_id).first()
        if edit_form.validate_on_submit():
            changed_rating = edit_form.rating.data
            book_to_update_by_filter.rating = changed_rating
            db.session.commit()
            return redirect('/')
    return render_template('edit.html', book=book, form=edit_form)


if __name__ == '__main__':
    with App.app_context():
        db.create_all()
    app.run(debug=True)
