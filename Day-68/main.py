from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from database import db, User, App

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'

# CREATE TABLE IN DB

# Line below only required once, when creating DB.
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    with App.app_context():
        if request.method == "POST":
            password = request.form.get('password')
            hashed_pass = generate_password_hash(password=password, method="pbkdf2:sha256", salt_length=8)
            new_user = User(
                email=request.form.get('email'),
                name=request.form.get('name'),
                password=hashed_pass
            )
            db.session.add(new_user)
            db.session.commit()
            return render_template('secrets.html', name=new_user.name)
    return render_template("register.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/secrets')
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    return send_from_directory('./static/files', 'cheat_sheet.pdf', as_attachment=True)


if __name__ == "__main__":
    with App.app_context():
        db.create_all()
    app.run(debug=True)
