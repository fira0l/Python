import datetime

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from database import App, db, BlogPost
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import os



## Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = "This is my secret key for my forms using csrf"
ckeditor = CKEditor(app)
Bootstrap(app)

# WTForm


class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    with App.app_context():
        posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    with App.app_context():
        requested_post = BlogPost.query.filter_by(id=index).first()
        print(requested_post)
        return render_template("post.html", post=requested_post)


@app.route('/new_post', methods=["GET", "POST"])
def new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        blog_title = form.title.data
        blog_subtitle = form.subtitle.data
        blog_body = form.body.data
        blog_img_url = form.img_url.data
        blog_author = form.author.data
        with App.app_context():
            new_blog = BlogPost(
                title=blog_title,
                subtitle=blog_subtitle,
                date=datetime.datetime.now().strftime("%B %d, %Y"),
                body=blog_body,
                author=blog_author,
                img_url=blog_img_url
            )
            db.session.add(new_blog)
            db.session.commit()
            return redirect('/')

    return render_template('make-post.html', form=form)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route('/edit_post/<int:post_id>', methods=["GET", "POST"])
def edit_post(post_id):
    with App.app_context():
        post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
        )
    if edit_form.validate_on_submit():
        with App.app_context():
            post = BlogPost.query.get(post_id)
            post.title = edit_form.title.data
            post.subtitle = edit_form.subtitle.data
            post.img_url = edit_form.img_url.data
            post.author = edit_form.author.data
            post.body = edit_form.body.data
            db.session.commit()
            return redirect(url_for("show_post", index=post.id))
    return render_template('make-post.html', form=edit_form, is_edit=True)


if __name__ == "__main__":
    with App.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
