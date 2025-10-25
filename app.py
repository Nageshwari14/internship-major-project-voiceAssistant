from flask import Flask, request, jsonify
from flask_cors import CORS
from main import process_command

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "✅ Flask backend is running successfully!"

@app.route("/command", methods=["POST"])
def command():
    data = request.get_json()
    command_text = data.get("command", "").lower().strip()
    response = process_command(command_text)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
