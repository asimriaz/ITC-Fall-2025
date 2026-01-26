from flask import Flask, jsonify, request, render_template
import json

app = Flask(__name__)

countries = []

# Load countries from JSON
def load_countries():
    global countries
    with open('countries.json', 'r') as f:
        countries = json.load(f)

load_countries()

@app.route("/")
def index():
    return render_template('index.html')

# Get all countries
@app.route("/api/countries")
def get_countries():
    return jsonify(countries)

# Get country by ID
@app.route("/api/countries/<int:id>")
def get_country(id):
    for c in countries:
        if c['countryid'] == id:
            return jsonify(c)
    return jsonify({"error": "Country not found"}), 404

# Save/update country
@app.route("/api/countries/save", methods=['POST'])
def save_country():
    updated = request.get_json()
    updated['countryid'] = int(updated['countryid'])

    for i, c in enumerate(countries):
        if c['countryid'] == updated['countryid']:
            countries[i] = updated
            return jsonify({"message": "Country updated successfully"}), 200

    return jsonify({"error": "Country not found"}), 404

# Search countries
@app.route("/api/countries/search", methods=['POST'])
def search_countries():
    criteria = request.get_json()
    name = criteria.get('name', '').lower()
    filtered = [c for c in countries if name in c['name'].lower()]
    return jsonify(filtered)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5500)
