import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Omni Python Backend is active 24/7!"})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json or {}
    msg = data.get("message", "").strip()
    if not msg:
        return jsonify({"reply": ""})

    clean = msg.lower()
    if "who created you" in clean:
        return jsonify({"reply": "I was created by Vedant."})
    if "who are you" in clean:
        return jsonify({"reply": "I am Omni, your 24/7 AI assistant."})

    return jsonify({"reply": f"Omni received: {msg}"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
