# Cafes Plus

## Project Description

**Cafes Plus** is a web project that uses **Flask** and **Bootstrap** to create a site for adding and viewing cafe data. It allows users to input information about cafes such as cafe name, location, working hours, wifi quality, and power availability, and then displays this data in a table.

## How to Use the Project

1. **Add a New Cafe:**
   To start adding a new cafe to the database, visit the following URL:
   `http://<your-host>/add`
   Or if you're running the app locally:
   `http://127.0.0.1:5000/add`
   
   A form will be available to input the required information such as the cafe name, location, working hours, wifi availability, and power availability.

2. **View Cafes:**
   To view all the cafes that have been added, visit the following URL:
   `http://<your-host>/cafes`
   Or if you're running the app locally:
   `http://127.0.0.1:5000/cafes`
   
   This page will display all cafes in a table format.

## Installation

### 1. Install the Requirements:
   Ensure you have **Python** and **pip** installed on your system. Then install the necessary dependencies by running:
   ```bash
   pip install -r requirements.txt
  ```

### 2. Run the Application:
To start the application, run:
```bash
   python main.py
  ```
After starting the app, you can access it in your browser at http://127.0.0.1:5000.

## Technologies Used
- Flask: For building the web application.
- Bootstrap: For enhancing the user interface design.
- WTForms: For creating forms and validating input.
- CSV: For storing cafe data in a CSV file.
