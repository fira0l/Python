from flask import Flask, render_template, request

app = Flask(__name__)


def form_handler(username, password):
    password = password
    return render_template('success.html', username=username, password=password)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['Post'])
def login_handler():
    error = None
    username = request.form['username']
    password = request.form['password']
    return form_handler(username, password)


if __name__ == "__main__":
    app.run(debug=True)