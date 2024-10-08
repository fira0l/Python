from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TimeField, SelectField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


def coffe_rating_function():
    coffe_r = []
    for i in range(0, 6):
        rating = "☕" * i
        coffe_r.append((i, f"{rating}"))
    return tuple(coffe_r)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    Location = StringField('Location URL', validators=[DataRequired()])
    opentime = TimeField('Opening Time', validators=[DataRequired()])
    closingtime = TimeField('Closing Time', validators=[DataRequired()])
    coffeerating = SelectField("Coffee Rating",
                               choices=[("✘", "✘"), ('☕', '☕'), ('☕☕', '☕☕'), ('☕☕☕', '☕☕☕'), ('☕☕☕☕', '☕☕☕☕'), ('☕☕☕☕☕', '☕☕☕☕☕')],
                               validators=[DataRequired()])
    wifirating = SelectField("Wifi Rating", choices=[("✘", "✘"), ('💪', '💪'), ('💪💪', '💪💪'), ('💪💪💪', '💪💪💪'), ('💪💪💪💪', '💪💪💪💪'),
                             ('💪💪💪💪💪', '💪💪💪💪💪')], validators=[DataRequired()])
    powerrating = SelectField("Power Rating", choices=[("✘", "✘"), ("🔌", "🔌"), ("🔌🔌", "🔌🔌"), ("🔌🔌🔌", "🔌🔌🔌"), ("🔌🔌🔌🔌", "🔌🔌🔌🔌"), ("🔌🔌🔌🔌🔌", "🔌🔌🔌🔌🔌")], validators=[DataRequired()])
    submit = SubmitField('Submit')

             # Exercise:
             # add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
             # make coffee/wifi/power a select element with choice of 0 to 5.
             # e.g. You could use emojis ☕️/💪/✘/🔌
             # make all fields required except submit
             # use a validator to check that the URL field has a URL entered.
             # ---------------------------------------------------------------------------

             # all Flask routes below


@ app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["Get", "Post"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe_name = form.cafe.data
        cafe_location = form.Location.data
        open_time = form.opentime.data
        close_time = form.closingtime.data
        coffe_rating = str(form.coffeerating.data)
        wifi_rating = str(form.wifirating.data)
        power_rating = str(form.powerrating.data)
        with open('cafe-data.csv', newline='', mode='a') as csv_file:
            csv_file.writelines(
                f'\n{cafe_name},{cafe_location},{open_time},{close_time},{coffe_rating.encode("utf-8")},{wifi_rating.encode("utf-8")},{power_rating.encode("utf-8")}')
        return "SuccessFully Submitted"
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
