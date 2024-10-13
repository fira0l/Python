from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,FloatField
from wtforms.validators import DataRequired

from database import App, db, Movie

app = Flask(__name__)
app.config["SECRET_KEY"] = "thisismysecretkey"
Bootstrap(app)


class RateMovieForm(FlaskForm):
    rating = FloatField("Your Rating out of 10 e.g 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    sumit = SubmitField("Submit")


@app.route('/')
def home():
    with App.app_context():
        movies = Movie.query.all()

    return render_template('index.html',movies=movies)


@app.route('/add')
def add():
    with App.app_context():
        new_movie = Movie(
            title="Phone Booth",
            year=2002,
            description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
            rating=7.3,
            ranking=10,
            review="My favourite character was the caller.",
            img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
        )
        db.session.add(new_movie)
        db.session.commit()
    return render_template('add.html')


@app.route('/select')
def select():
    return render_template('select.html')


@app.route('/edit/<int:movie_id>', methods=["GET", "POST"])
def edit(movie_id):
    form = RateMovieForm()
    if form.validate_on_submit():
        with App.app_context():
            movie_to_update = Movie.query.get(movie_id)
            movie_to_update.rating = form.rating.data
            movie_to_update.review = form.review.data
            db.session.commit()
            return redirect('/')
    return render_template('edit.html', form=form)


@app.route('/delete/<int:movie_id>')
def delete(movie_id):
    with App.app_context():
        movie_to_delete = Movie.query.get(movie_id)
        db.session.delete(movie_to_delete)
        db.session.commit()
        return redirect('/')


if __name__ == "__main__":
    with App.app_context():
        db.create_all()
    app.run(debug=True)
