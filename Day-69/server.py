import base64

from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_login import LoginManager

from database import db, App, User, BlogPost

app = Flask(__name__)
app.config["SECRET_KEY"] = "This_is_my_secret_key_for_my_website"
ckeditor = CKEditor(app)
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    with App.app_context():
        return User.query.get(int(user_id))

@app.route('/')
def get_all_posts():
    with App.app_context():
        posts = BlogPost.query.all()
        return render_template('index.html', all_posts=posts)


if __name__ == "__main__":
    with App.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
