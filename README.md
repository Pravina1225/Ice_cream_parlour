This is a simple Ice Cream Shop Web Application built using Flask, SQLite, HTML, CSS, and
JavaScript.
The application allows users to view available ice cream flavors, add them to the cart, and view their
cart items. It includes dynamic offerings based on season, and flavors can be filtered by season.
1. Dependencies and Installation:
 1. Python 3.11 or higher
 2. Flask (Web framework)
 3. SQLite (Database for storing flavors and cart data)
 4. HTML, CSS, JavaScript (Frontend)
2.To run the application, follow these steps:
 1. Clone the repository or download the application files.
 2. Install the required dependencies by running the following command:
     pip install -r requirements.txt
     Flask: Web framework for backend development.
     SQLite: Database used to store ice cream flavors and cart information.
3. Database setup:
 - The SQLite database file (`ice_cream.db`) should be located at `D:/4th sem/final/ice_cream.db`.
 - Ensure that the database exists, and contains the necessary tables (`flavors`, `cart`).
 - If the database or tables are missing, the application will raise errors. You can manually create
the database or use a script to initialize it.
4. Running the application:
 To start the application, run the following command:
  python app.py
  This will start the Flask development server.
5.Dependencies (in requirements.txt):
 Flask==2.2.2
 sqlite3

