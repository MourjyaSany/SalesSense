from flask import Flask, request, jsonify
from flask_cors import CORS
from backend.database import init_db, add_lead, get_leads  # Updated import
from backend.lead_scoring import score_lead  # Ensure correct import path

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Requests

@app.route("/")
def home():
    return "Welcome to SalesSense AI CRM Backend!"

@app.route("/score", methods=["POST"])
def get_lead_score():
    data = request.json
    
    # Ensure all required fields are present
    required_fields = ["age", "income", "website_visits", "email_clicks"]
    if not data or not all(field in data for field in required_fields):
        return jsonify({"error": f"Invalid request. Required fields: {required_fields}"}), 400

    lead_score = score_lead(data)
    return jsonify({"lead_score": lead_score})

@app.route("/leads", methods=["GET"])
def fetch_leads():
    leads = get_leads()
    return jsonify(leads)

@app.route("/add_lead", methods=["POST"])
def add_new_lead():
    data = request.json
    if "name" not in data or "email" not in data:
        return jsonify({"error": "Missing name or email"}), 400
    
    lead_id = add_lead(data["name"], data["email"], data.get("score", 0))
    return jsonify({"message": "Lead added!", "lead_id": lead_id})

if __name__ == "__main__":
    init_db()  # Initialize DB on startup
    app.run(debug=True)

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Requests

@app.route("/")
def home():
    return "Welcome to SalesSense AI CRM Backend!"

@app.route("/score", methods=["POST"])
def get_lead_score():
    data = request.json  # Get JSON from request
    
    # Required fields for scoring
    required_fields = ["age", "income", "website_visits", "email_clicks"]
    
    # Check if all fields exist in request
    if not data or not all(field in data for field in required_fields):
        return jsonify({"error": f"Invalid request. Required fields: {required_fields}"}), 400

    lead_score = score_lead(data)  # Pass the entire JSON object to the model
    return jsonify({"lead_score": lead_score})

@app.route("/leads", methods=["GET"])
def fetch_leads():
    leads = get_leads()
    return jsonify(leads)

@app.route("/add_lead", methods=["POST"])
def add_new_lead():
    data = request.json
    if "name" not in data or "email" not in data:
        return jsonify({"error": "Missing name or email"}), 400
    
    lead_id = add_lead(data["name"], data["email"], data.get("score", 0))
    return jsonify({"message": "Lead added!", "lead_id": lead_id})

if __name__ == "__main__":
    init_db()  # Initialize DB on startup
    app.run(debug=True)
