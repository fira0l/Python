from flask import Flask, render_template
import requests

app = Flask(__name__)

API_URL = "https://api.npoint.io/a08e70ad31bd4e7dca38"


@app.route('/')
def home():
    response = requests.get(url=API_URL)
    blog_data = response.json()
    return render_template('index.html', blog_data=blog_data)


@app.route('/post')
def post():
    return render_template('post.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)