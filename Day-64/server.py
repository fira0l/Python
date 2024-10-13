from flask import Flask, render_template, redirect
import requests
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, IntegerField
from wtforms.validators import DataRequired

from database import App, db, Movie

TMDB_URL = "https://api.themoviedb.org/3/search/movie"

app = Flask(__name__)
app.config["SECRET_KEY"] = "thisismysecretkey"
Bootstrap(app)

Movies = []

class RateMovieForm(FlaskForm):
    rating = FloatField("Your Rating out of 10 e.g 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Submit")


class AddMovieForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/')
def home():
    with App.app_context():
        movies = Movie.query.all()
    return render_template('index.html', movies=movies)


@app.route('/add', methods=["GET", "POST"])
def add():
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmOGI5ZjAzNWMwYzQ4OWI5ZDZkNGQ3ZjFiNjZlOTgwMCIsIm5iZiI6MTcyODgzMjUxNi43OTkyODQsInN1YiI6IjY3MGJlMTYyYjE1ZDk3YjFhOTNjOTk0NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.F7P-Pc2DQMuCOupRfqg93vhYlbaHV7pjBA18ciJO0-U"
    }
    form = AddMovieForm()
    if form.validate_on_submit():
        title = form.title.data
        params = {
            "query": title,
            "include_adult": False
        }
        response = requests.get(url=TMDB_URL, params=params, headers=headers)
        movie_data = response.json()
        print(movie_data)
        movie = movie_data["results"]
        Movies.append(movie)
        result_movie = movie[0]
        year = result_movie["release_date"].split('-')[0]
        return render_template('select.html', data=movie)
        # with App.app_context():
        #     new_movie = Movie(
        #         title=result_movie["title"],
        #         description=result_movie["overview"],
        #         rating=result_movie["vote_average"],
        #         review="Awesome Movie",
        #         year=year,
        #         ranking=3,
        #         img_url=f"https://image.tmdb.org/t/p/w300_and_h450_bestv2/{result_movie["poster_path"]}"
        #     )
        #     db.session.add(new_movie)
        #     db.session.commit()
        #     return render_template('select.html', data=movie)
    # with App.app_context():
    #     db.session.add(new_movie)
    #     db.session.commit()
    #     return redirect('/')
    return render_template('add.html', form=form)


@app.route('/select')
def select():
    with App.app_context():
        new_movie = Movie(
            title=movie["title"],
            description=movie["overview"],
            rating=movie["vote_average"],
            review="Awesome Movie",
            year=year,
            ranking=3,
            img_url=f"https://image.tmdb.org/t/p/w300_and_h450_bestv2/{movie["poster_path"]}"
        )
        db.session.add(new_movie)
        db.session.commit()
    return render_template('select.html')


@app.route('/edit/<int:movie_id>', methods=["GET", "POST"])
def edit(movie_id):
    form = RateMovieForm()
    if form.validate_on_submit():
        with App.app_context():
            if Movie.query.filter_by(id=movie_id) == "":
                new_movie = Movie(rating=form.rating.data, review=form.review.data)
                db.session.add(new_movie)
                db.session.commit()
            else:
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
