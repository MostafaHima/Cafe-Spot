# Importing required modules
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from add import CafeForm
import csv

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# Route for the home page
@app.route("/")
def home():
    return render_template("index.html")

# Route for adding a new cafe
@app.route('/add', methods=["POST", "GET"])
def add_cafe():
    form = CafeForm()  # Initialize the form
    # Check if the form is submitted and validated
    if form.validate_on_submit():

        # Get data from the form
        caffe_name = form.cafe_name.data
        location = form.location.data
        power = form.power.data
        wifi = form.wifi.data
        coffee = form.coffee.data
        open_ = form.open.data
        close = form.close.data

        # Write the cafe data to the CSV file
        with open("cafe-data.csv", newline="", mode="a", encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([caffe_name, location, open_, close, coffee, wifi, power])

        # Redirect to the add cafe page after form submission
        return redirect(url_for('add_cafe'))
    # Render the 'add' page with the form
    return render_template('add.html', form=form)

# Route for displaying a list of all cafes
@app.route('/cafes')
def cafes():
    # Read the data from the CSV file
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        # Append each row to the list
        for row in csv_data:
            list_of_rows.append(row)
    # Render the cafes page with the list of cafes
    return render_template('cafes.html', cafes=list_of_rows)

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
