import datetime

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from database import App, db, BlogPost
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField


## Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
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


@app.route('/edit_post/<int:post_id>')
def edit_post(post_id):
    pass


if __name__ == "__main__":
    with App.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)