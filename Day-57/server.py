from flask import Flask,render_template
from _datetime import datetime

app = Flask(__name__)

current_year = datetime.now()


@app.route('/')
def home():
    return render_template('index.html',year=current_year.year)


@app.route('/guess/<name>')
def guess(name):



if __name__ == "__main__":
    app.run(debug=True)