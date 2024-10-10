from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add')
def add():
    return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)