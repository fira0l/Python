from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def make_underline(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route('/')
@make_emphasis
@make_underline
def hellow_world():
    return ("<div> \
    <h1>Hello World</h1><br/>\
    <p>This a Test Paragraph For Flask</p> \
    <img src='https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWU1ZWE3cmFxOW03enF1NG12eXRhempuMGRkcmtnMW5lN3czNnpwdSZ"
            "lcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/v4F8XAvnH7BZKBjhDG/giphy.webp' alt='A Text'> \
    <div>")


@app.route('/bye')
def bye():
    return "<h1>Good Bye, For Visiting</h1>"


@app.route('/greet/<name>/<number>')
def greet(name,number):
    return f"Hello there {name}, You are {number} years old"


if __name__ == "__main__":
    app.run(debug=True)
