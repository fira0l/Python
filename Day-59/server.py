from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)

API_URL = "https://api.npoint.io/a08e70ad31bd4e7dca38"
Author = "Firaol A."
today = datetime.now().strftime('%B %d, %Y')
response = requests.get(url=API_URL)
blog_data = response.json()


@app.route('/')
def home():
    return render_template('index.html', blog_data=blog_data, date=today, author=Author)


@app.route('/post')
def post():
    return render_template('index.html', blog_data=blog_data, date=today, author=Author)


@app.route('/post/<int:post_id>')
def single_post(post_id):
    post = {}
    for blog in blog_data:
        if blog['id'] == post_id:
            post = blog
    return render_template('post.html', post=post, author=Author, date=today)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)