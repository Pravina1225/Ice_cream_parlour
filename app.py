
from flask import Flask, render_template, request, redirect, url_for, jsonify
from models import query_db, add_to_cart, get_cart, add_allergen

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    try:
        flavors = query_db("SELECT * FROM flavors")
    except Exception as e:
        print(f"Error fetching flavors: {e}")
        flavors = []
    return render_template("index.html", flavors=flavors)

# Cart route
@app.route("/cart")
def cart():
    try:
        cart_items = get_cart()
    except Exception as e:
        print(f"Error fetching cart items: {e}")
        cart_items = []
    return render_template("cart.html", cart=cart_items)

# Add to cart route
@app.route("/add_to_cart/<int:flavor_id>")
def add_to_cart_route(flavor_id):
    try:
        add_to_cart(flavor_id)
    except Exception as e:
        print(f"Error adding flavor to cart: {e}")
    return redirect(url_for('cart'))

# Offerings route with seasonal filter
@app.route("/offerings")
def offerings():
    seasonal = request.args.get('season')
    query = "SELECT * FROM flavors"
    if seasonal:  # Apply season filter
        query += " WHERE season = ?"
        try:
            flavors = query_db(query, (seasonal,))
        except Exception as e:
            print(f"Error fetching seasonal flavors: {e}")
            flavors = []
    else:  # Fetch all flavors
        try:
            flavors = query_db(query)
        except Exception as e:
            print(f"Error fetching flavors: {e}")
            flavors = []
    return render_template("offerings.html", flavors=flavors)

# Add allergen route
@app.route("/add_allergen", methods=["POST"])
def add_allergen_route():
    allergen = request.form.get("allergen")
    try:
        add_allergen(allergen)
    except Exception as e:
        print(f"Error adding allergen: {e}")
    return redirect(url_for('home'))

# Suggestions route for getting and submitting flavor ideas
@app.route("/suggestions", methods=["POST", "GET"])
def suggestions():
    if request.method == "POST":
        name = request.form.get("name")
        suggestion = request.form.get("suggestion")
        try:
            query_db("INSERT INTO suggestions (name, suggestion) VALUES (?, ?)", (name, suggestion))
        except Exception as e:
            print(f"Error submitting suggestion: {e}")
        return redirect(url_for("home"))
    
    try:
        suggestions = query_db("SELECT * FROM suggestions")
    except Exception as e:
        print(f"Error fetching suggestions: {e}")
        suggestions = []
    
    return render_template("suggestions.html", suggestions=suggestions)

if __name__ == "__main__":
    app.run(debug=True)

