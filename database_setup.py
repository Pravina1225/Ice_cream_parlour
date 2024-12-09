import sqlite3

def setup_database():
    conn = sqlite3.connect("ice_cream.db")
    cursor = conn.cursor()

    # Create tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS flavors (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        season TEXT NOT NULL,
        description TEXT NOT NULL,
        image TEXT NOT NULL,
        price INTEGER NOT NULL
    )
''')
 
    cursor.execute('''CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ingredient TEXT UNIQUE NOT NULL,
        quantity INTEGER NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS allergens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        allergen TEXT UNIQUE NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS suggestions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        suggestion TEXT NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS cart (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        flavor_id INTEGER,
        FOREIGN KEY (flavor_id) REFERENCES flavors(id)
    )''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
