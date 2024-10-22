import os
from flask import Flask, render_template, redirect, url_for, flash, abort
from functools import wraps
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date, datetime
from werkzeug.security import generate_password_hash, check_password_hash
from forms import CreatePostForm, UserSignUpForm, LoginForm, CommentForm
import gravatar
from database import db, BlogPost, App, User
from flask_login import LoginManager, login_user, login_required, current_user, logout_user

app = Flask(__name__)
app.secret_key = "Thisismysecretkeysoenjoyit"
ckeditor = CKEditor(app)
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)


def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        #If id is not 1 then return abort with 403 error
        if current_user.id != 1:
            return abort(403)
        #Otherwise continue with the route function
        return f(*args, **kwargs)
    return decorated_function


@login_manager.user_loader
def load_user(user_id):
    with App.app_context():
        user = User.query.get(int(user_id))
        return user


@app.route('/')
def get_all_posts():
    with App.app_context():
        posts = BlogPost.query.all()
        return render_template("index.html", all_posts=posts, current_user=current_user)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = UserSignUpForm()
    if form.validate_on_submit():
        username = form.username.data
        user_email = form.email.data
        user_password = form.password.data
        hashed_password = generate_password_hash(password=user_password, method="pbkdf2:sha256", salt_length=8)
        with App.app_context():
            if User.query.filter_by(email=user_email).first():
                flash("You've already Signed up with that email, please login instead!")
                return redirect(url_for('login'))

            new_user = User(
                name=username,
                email=user_email,
                password=hashed_password
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('get_all_posts'))
    return render_template("register.html", form=form, current_user=current_user)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        with App.app_context():
            user = User.query.filter_by(email=form.email.data).first()
            if not user:
                flash("The email doesn't exist, please try again.")
                return redirect(url_for('login'))
            elif not check_password_hash(user.password, form.password.data):
                flash("Password incorrect, please try again.")
                return redirect(url_for('login'))
            else:
                login_user(user)
                return redirect(url_for('get_all_posts'))
    return render_template("login.html", form=form, current_user=current_user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@app.route("/post/<int:post_id>",methods=['GET', 'POST'])
def show_post(post_id):
    comment_form = CommentForm()
    with App.app_context():
        requested_post = BlogPost.query.get(post_id)
        author = User.query.filter_by(id=requested_post.author_id).first()
    return render_template("post.html", post=requested_post, current_user=current_user, form=comment_form, author=author)


@app.route("/about")
def about():
    return render_template("about.html", current_user=current_user)


@app.route("/contact")
def contact():
    return render_template("contact.html", current_user=current_user)


@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        with App.app_context():
            new_post = BlogPost(
                title=form.title.data,
                subtitle=form.subtitle.data,
                body=form.body.data,
                img_url=form.img_url.data,
                author=current_user,
                date=date.today().strftime("%B %d, %Y")
            )
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form, current_user=current_user)


@app.route("/edit-post/<int:post_id>", methods=["GET","POST"])
@admin_only
def edit_post(post_id):
    with App.app_context():
        post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        # author=post.author_id,
        body=post.body
    )
    with App.app_context():
        post = BlogPost.query.get(post_id)
        if edit_form.validate_on_submit():
            post.title = edit_form.title.data
            post.subtitle = edit_form.subtitle.data
            post.img_url = edit_form.img_url.data
            # post.author = edit_form.author.data
            post.body = edit_form.body.data
            db.session.commit()
            return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form, is_edit=True, current_user=current_user)


@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    with App.app_context():
        post_to_delete = BlogPost.query.get(post_id)
        db.session.delete(post_to_delete)
        db.session.commit()
        return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    with App.app_context():
        db.create_all()
    app.run(debug=True)
