from flask import Flask, request, jsonify
from flask_cors import CORS
from backend.database import init_db, add_lead, get_leads  # Ensure correct import
from backend.lead_scoring import score_lead  # Ensure correct import

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Requests

# Debugging: Print registered API routes
print("✅ Registered API Routes:")
for rule in app.url_map.iter_rules():
    print(rule, "-->", ", ".join(rule.methods))

@app.route("/")
def home():
    return "Welcome to SalesSense AI CRM Backend!"

@app.route("/score", methods=["GET", "POST", "OPTIONS"])  # Allow multiple methods for testing
def get_lead_score():
    if request.method == "OPTIONS":
        return jsonify({"message": "CORS preflight request received"}), 200

    if request.method != "POST":
        return jsonify({"error": "Only POST requests are allowed!"}), 405
    
    data = request.json
    required_fields = ["age", "income", "website_visits", "email_clicks"]

    if not data or not all(field in data for field in required_fields):
        return jsonify({"error": f"Invalid request. Required fields: {required_fields}"}), 400

    lead_score = score_lead(data)
    return jsonify({"lead_score": lead_score})

@app.route("/leads", methods=["GET"])
def fetch_leads():
    leads = get_leads()
    return jsonify(leads)

@app.route("/add_lead", methods=["GET", "POST", "OPTIONS"])  # Allow OPTIONS for debugging
def add_new_lead():
    if request.method == "OPTIONS":
        return jsonify({"message": "CORS preflight request received"}), 200

    if request.method != "POST":
        return jsonify({"error": "Only POST requests are allowed!"}), 405

    data = request.json
    if "name" not in data or "email" not in data:
        return jsonify({"error": "Missing name or email"}), 400
    
    lead_id = add_lead(data["name"], data["email"], data.get("score", 0))
    return jsonify({"message": "Lead added!", "lead_id": lead_id})

if __name__ == "__main__":
    init_db()  # Initialize DB on startup
    app.run(debug=True)
