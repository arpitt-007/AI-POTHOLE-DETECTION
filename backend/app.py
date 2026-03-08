import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "..", "data", "potholes.json")

# Read stored potholes
def read_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# Save potholes
def write_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route("/add_pothole", methods=["POST"])
def add_pothole():

    potholes = read_data()
    data = request.json

    potholes.append(data)

    write_data(potholes)

    return {"status": "saved"}

@app.route("/get_potholes", methods=["GET"])
def get_potholes():

    potholes = read_data()

    return jsonify(potholes)

@app.route("/add_demo")
def add_demo():

    potholes = read_data()

    data = {
        "lat": 13.0827,
        "lon": 80.2707,
        "time": "demo"
    }

    potholes.append(data)

    write_data(potholes)

    return {"message": "Demo pothole added"}

if __name__ == "__main__":
    app.run(debug=True)