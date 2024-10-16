import random
from database import db, App, Cafe
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route('/random', methods=["GET"])
def get_random_cafe():
    with App.app_context():
        cafes = Cafe.query.all()
        print(cafes)
        random_cafe = random.choice(cafes)
        jsondata = jsonify(cafe=random_cafe.to_dict())
        return jsondata


## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    with App.app_context():
        db.create_all()
    app.run(debug=True)
