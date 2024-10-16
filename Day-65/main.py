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
        jsondata = jsonify(cafe={"id": random_cafe.id,
                                 "name": random_cafe.name,
                                 "map_url": random_cafe.map_url,
                                 "img_url": random_cafe.img_url,
                                 "location": random_cafe.location,
                                 "seats": random_cafe.seats,
                                 "has_toilet": random_cafe.has_toilet,
                                 "has_wifi": random_cafe.has_wifi,
                                 "has_sockets": random_cafe.has_sockets,
                                 "can_take_calls": random_cafe.can_take_calls,
                                 "coffee_price": random_cafe.coffee_price, })
        return jsondata


## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    with App.app_context():
        db.create_all()
    app.run(debug=True)
