from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from database import App, db, Movie

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def home():
    return render_template('index.html')


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


@app.route('/edit')
def edit():
    return render_template('edit.html')


if __name__ == "__main__":
    with App.app_context():
        db.create_all()
    app.run(debug=True)
