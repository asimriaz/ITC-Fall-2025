from flask import Flask, jsonify, request, render_template
import json
import os

app = Flask(__name__, template_folder="templates")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "countries.json")

# Load data
with open(DATA_FILE, "r") as f:
    countries = json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/countries")
def get_countries():
    return jsonify(countries)

@app.route("/api/countries/save", methods=["POST"])
def save_country():
    updated = request.get_json()
    updated["countryid"] = int(updated["countryid"])

    for i, c in enumerate(countries):
        if c["countryid"] == updated["countryid"]:
            countries[i] = updated

            # optional: save back to file
            with open(DATA_FILE, "w") as f:
                json.dump(countries, f, indent=2)

            return jsonify({"message": "Country saved successfully"}), 200

    return jsonify({"error": "Country not found"}), 404

@app.route("/api/countries/search", methods=["POST"])
def search_countries():
    data = request.get_json()
    name = data.get("name", "").lower()
    return jsonify([c for c in countries if name in c["name"].lower()])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5500)
