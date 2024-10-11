from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

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
    return render_template('index.html')


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

    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
