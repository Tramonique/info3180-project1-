# flask_starter
Starter code for a new Flask Application

Remember to always create a virtual environment and install the packages in your requirements file

```bash
$ python -m venv venv (you may need to use python3 instead)
$ source venv/bin/activate (or .\venv\Scripts\activate on Windows)
$ pip install -r requirements.txt
$ flask --app app --debug run
```
📌 Project Title

INFO3180 Project 1 – Property Listing Web Application

📖 Description

This project is a Flask-based web application that allows users to create, store, and view property listings for rent or sale. The application uses a PostgreSQL database to store property information and supports image uploads for each listing.

Users can:

Add new properties using a validated form
Upload an image for each property
View a list of all properties
View detailed information for a specific property

⚙️ Technologies Used
Python (Flask)
Flask-WTF (form handling and validation)
Flask-SQLAlchemy (ORM)
Flask-Migrate (database migrations)
PostgreSQL
HTML / CSS / Bootstrap

🚀 Features
Create property listings with title, description, price, location, bedrooms, bathrooms, and type
Image upload and storage (filename saved in database)
Display all properties in a card layout
Individual property detail view
Flash messages for user feedback
Database migrations for reproducibility

🧭 Routes
/properties/create → Add a new property
/properties → View all properties
/properties/<propertyid> → View a single property
🗄️ Database

The application uses a PostgreSQL database with a Property model.
Migration files are included to recreate the database schema.

▶️ How to Run
Clone the repository
Create and activate a virtual environment

Install dependencies

pip install -r requirements.txt
Set up environment variables (e.g. database URI, secret key)

Run migrations

flask db upgrade

Start the server

flask run
📌 Notes
Uploaded images are stored locally and referenced in the database
The “Email Realtor” button is for display purposes only
