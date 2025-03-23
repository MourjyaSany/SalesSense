from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/score', methods=['POST'])
def get_lead_score():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400  # Ensure JSON content

    data = request.get_json()  # Get JSON safely

    if not data:
        return jsonify({"error": "Empty JSON body"}), 400

    lead_data = data.get("lead_data", "No data provided")
    return jsonify({"lead_score": lead_data})

@app.route('/')  
def home():
    return "Hello, Flask is running!"

if __name__ == '__main__':  
    app.run(debug=True)
