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


@app.route('/all')
def all_cafes():
    with App.app_context():
        cafes = Cafe.query.all()
        all_cafe = [cafe.to_dict() for cafe in cafes]
        return jsonify(Cafes=all_cafe)


@app.route('/search')
def search_cafe():
    with App.app_context():
        query_location = request.args.get("loc")
        cafe = Cafe.query.filter_by(location=query_location).first()
        if cafe:
            return jsonify(cafe=cafe.to_dict())
        else:
            return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})

## HTTP POST - Create Record


@app.route('/add', methods=["POST"])
def add_cafe():
    with App.app_context():
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("loc"),
            has_sockets=bool(request.form.get("sockets")),
            has_toilet=bool(request.form.get("toilet")),
            has_wifi=bool(request.form.get("wifi")),
            can_take_calls=bool(request.form.get("calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
        )
        db.session.add(new_cafe)
        db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    with App.app_context():
        db.create_all()
    app.run(debug=True)
