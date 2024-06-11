from utils import emoji, make_choices
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired


class CafeForm(FlaskForm):
    cafe_name = StringField("Cafe Name", validators=[DataRequired()])
    location_url = URLField(
        "Cafe Location on Google maps (url)", validators=[DataRequired(), URL()]
    )
    open = StringField("Opens at", validators=[DataRequired()])
    close = StringField("Closes at", validators=[DataRequired()])
    coffee = SelectField(
        "Coffee rating",
        validators=[DataRequired()],
        choices=make_choices(emoji["coffee"]),
    )
    power = SelectField(
        "Power rating",
        validators=[DataRequired()],
        choices=make_choices(emoji["power"]),
    )
    wifi = SelectField(
        "Wifi rating",
        validators=[DataRequired()],
        choices=make_choices(emoji["wifi"]),
    )
    submit = SubmitField("Submit")
