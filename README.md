# 📌 INFO3180 Project 1 – Property Listing Web Application

## 📖 Description

This project is a Flask-based web application that allows users to create, store, and view property listings for rent or sale. The application uses a PostgreSQL database to store property information and supports image uploads for each listing.

Users can:

- Add new properties using a validated form  
- Upload multiple images for each property  
- Select currency (JMD, USD, CAD)  
- View a list of all properties  
- View detailed information for a specific property  

---

## ⚙️ Technologies Used

- Python (Flask)  
- Flask-WTF (form handling and validation)  
- Flask-SQLAlchemy (ORM)  
- Flask-Migrate (database migrations)  
- PostgreSQL  
- HTML, CSS, Bootstrap  

---

## 🚀 Features

- Create property listings with title, description, price, location, bedrooms, bathrooms, and type  
- Currency selection (JMD, USD, CAD)  
- Multiple image uploads per property  
- Image carousel on property detail page  
- Image upload and storage (filenames saved in the database)  
- Display all properties in a card layout  
- Individual property detail view  
- Flash messages for user feedback  
- Responsive and styled user interface  
- Database migrations for reproducibility  

---

## 🧭 Routes

- `/properties/create` → Add a new property  
- `/properties` → View all properties  
- `/properties/<propertyid>` → View a single property  

---

## 🗄️ Database

The application uses a PostgreSQL database with a `Property` model and a related model for storing multiple property images.

Migration files are included so the database schema can be recreated.

---

## ▶️ How to Run

1. Clone the repository

git clone <your-repo-link>  
cd your-project  

2. Create and activate a virtual environment

python -m venv venv  
source venv/Scripts/activate  

3. Install dependencies

pip install -r requirements.txt  

4. Set up environment variables by creating a `.env` file in the project root:

FLASK_DEBUG=True  
FLASK_RUN_PORT=8080  
FLASK_RUN_HOST=0.0.0.0  
SECRET_KEY=your_secret_key  
DATABASE_URL=postgresql://postgres:yourpassword@localhost/property_db  

5. Create a PostgreSQL database (any name), then update the DATABASE_URL in the .env file accordingly.

6. Run migrations

flask db upgrade  

7. Start the server

flask run  

Then open your browser and go to:

http://127.0.0.1:8080  

---

## 📌 Notes

- The “Email Realtor” button is for display purposes only  
