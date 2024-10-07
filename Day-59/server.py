from flask import Flask, render_template,request
import requests
from datetime import datetime
from smtplib import SMTP

my_email = 'firaforpython@gmail.com'
my_password = "odsfplyzjibggmof"

app = Flask(__name__)

API_URL = "https://api.npoint.io/a08e70ad31bd4e7dca38"
Author = "Firaol A."
today = datetime.now().strftime('%B %d, %Y')
response = requests.get(url=API_URL)
blog_data = response.json()


def send_msg(name, email, phone, message):
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="firaolanbessa170@gmail.com",
            msg=f"Subject:{name} Contacted U\n\n email: {email}\n phone: {phone}\n\nmessage: {message}"
        )
    return f"<h1>Successfully sent to THe Owner. They will contact u back. Thank you For reaching out {name} </h1>"


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


@app.route('/contact-us', methods=["post"])
def contact_me():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    return send_msg(name, email, phone, message)


if __name__ == "__main__":
    app.run(debug=True)