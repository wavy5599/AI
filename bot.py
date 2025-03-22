import openai
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS

# Load environment variables
load_dotenv()

# Initialize Flask app and CORS
app = Flask(__name__)
CORS(app)  # ✅ Enable CORS for all routes

# Set OpenAI API Key
openai.api_key = os.getenv('key')
FRONTEND_PASSWORD = os.getenv('FRONTEND_PASSWORD')  # For client auth

@app.route('/')
def home():
    return "Flask server with AI Chatbot is running!"

@app.route('/validate-password', methods=['POST'])
def validate_password():
    data = request.get_json()
    submitted_password = data.get('password')
    if submitted_password == FRONTEND_PASSWORD:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False}), 403

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message")

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": user_message}]
        )
        bot_reply = response["choices"][0]["message"]["content"]
        return jsonify({"reply": bot_reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
