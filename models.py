import sqlite3

def query_db(query, args=(), one=False):
    conn = sqlite3.connect("D:\\4th sem\\final\\ice_cream.db")
    cursor = conn.cursor()
    cursor.execute(query, args)
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return (result[0] if result else None) if one else result

def add_to_cart(flavor_id):
    query_db("INSERT INTO cart (flavor_id) VALUES (?)", (flavor_id,))

def get_cart():
    return query_db("SELECT f.name FROM cart c JOIN flavors f ON c.flavor_id = f.id")

def add_allergen(allergen):
    query_db("INSERT OR IGNORE INTO allergens (allergen) VALUES (?)", (allergen,))

def get_all_allergens():
    return query_db("SELECT allergen FROM allergens")
