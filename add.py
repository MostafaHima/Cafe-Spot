
# Import necessary modules for Flask forms
from flask_wtf.form import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL


# Define the form for adding cafe details
class CafeForm(FlaskForm):
    # Field for cafe name with a required validator
    cafe_name = StringField(label='Cafe Name', validators=[DataRequired(message="This field is required"), ])

    # Field for cafe location (Google Maps URL) with required and URL format validation
    location = StringField(label='Cafe Location On Google Maps (URL)',
                           validators=[DataRequired(message='This field is required'), URL(message="Invalid url")])

    # Field for cafe opening time with a required validator
    open = StringField(label='Open', validators=[DataRequired()])

    # Field for cafe closing time with a required validator
    close = StringField(label='Close', validators=[DataRequired()])

    # Field for coffee options with predefined choices (emoji-based)
    coffee = SelectField(label='Coffee', choices=[
        ("☕", "☕️"),
        ("☕️☕️", "☕☕️"),
        ("☕☕️☕️", "☕☕☕️"),
        ("☕☕☕️☕️", "☕☕☕☕️"),
        ("☕☕☕☕️☕️", "☕☕☕☕️☕️")
    ])

    # Field for wifi options with predefined choices (emoji-based)
    wifi = SelectField(label='Wifi', choices=[
        ("💪", "💪"),
        ("💪💪", "💪💪"),
        ("💪💪💪", "💪💪💪"),
        ("💪💪💪💪", "💪💪💪💪"),
        ("💪💪💪💪💪", "💪💪💪💪💪"),
    ])

    # Field for power options with predefined choices (emoji-based)
    power = SelectField(label='Power', choices=[
        ("🔌", "🔌"),
        ("🔌🔌", "🔌🔌"),
        ("🔌🔌🔌", "🔌🔌🔌"),
        ("🔌🔌🔌🔌", "🔌🔌🔌🔌"),
        ("🔌🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"),
    ])

    # Submit button for the form
    submit = SubmitField(label="Submit")
