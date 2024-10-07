from flask import Flask,render_template
from _datetime import datetime
import requests

AGIFY_URL = "https://api.agify.io"
GENDERIZE_URL = "https://api.genderize.io"

app = Flask(__name__)

current_year = datetime.now()


@app.route('/')
def home():
    return render_template('index.html',year=current_year.year)


@app.route('/guess/<name>')
def get_guess(name):
    params = {
        "name": name
    }
    response = requests.get(url=AGIFY_URL, params=params)
    user_data = response.json()
    gen_response = requests.get(url=GENDERIZE_URL, params=params)
    user_gender = gen_response.json()
    # print(user_data,user_gender)
    username = name.title()
    age = user_data["age"]
    gender = user_gender["gender"]
    return render_template('guess.html', user_name=username, age=age, gender=gender)



@app.route('/blog')
def get_blog():
    blog_url = " https://api.npoint.io/931bc6bfc3664f40ccc6"
    response = requests.get(url=blog_url)
    blog_data = response.json()
    print(blog_data)
    blog_title = blog_data[0]["title"]
    blog_subtitle = blog_data[0]["subtitle"]
    return render_template('blog.html', title=blog_title, subtitle=blog_subtitle, blog_post=blog_data )


if __name__ == "__main__":
    app.run(debug=True)