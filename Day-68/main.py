from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from database import db, User, App

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
login_manager = LoginManager()
login_manager.init_app(app)


# CREATE TABLE IN DB

# Line below only required once, when creating DB.
# db.create_all()


@login_manager.user_loader
def load_user(user_id):
    with App.app_context():
        return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    with App.app_context():
        if request.method == "POST":
            if User.query.filter_by(email=request.form.get('email')).first():
                flash("You've already signed up with that email, log in instead!")
                return redirect(url_for('login'))

            password = request.form.get('password')
            hashed_pass = generate_password_hash(password=password, method="pbkdf2:sha256", salt_length=8)
            new_user = User(
                email=request.form.get('email'),
                name=request.form.get('name'),
                password=hashed_pass
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return render_template('secrets.html', name=new_user.name)
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    error = None
    success = None
    if request.method == "POST":
        user_email = request.form.get("email")
        user_password = request.form.get("password")
        with App.app_context():
            user = User.query.filter_by(email=user_email).first()
            if not user:
                flash("The email doesnt exist, please try again.")
                return redirect(url_for('login'))
            elif not check_password_hash(user.password, user_password):
                flash("Password incorrect, please try again.")
                return redirect(url_for('login'))
            else:
                login_user(user)
                return render_template('secrets.html', name=user.name)

    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('./static/files', 'cheat_sheet.pdf', as_attachment=True)


if __name__ == "__main__":
    with App.app_context():
        db.create_all()
    app.run(debug=True)
