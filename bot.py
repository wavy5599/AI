from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv
import re

# Load environment vars
load_dotenv()

# Flask app setup
app = Flask(__name__, static_folder='static')
CORS(app)

# Set OpenAI key
openai.api_key = os.getenv("key")
FRONTEND_PASSWORD = os.getenv("FRONTEND_PASSWORD")

# Session memory
user_memory = {"name": None, "bot_name": "Wavy's Bot"}
conversation_history = []

# Serve index.html at /
@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

# Serve other static assets
@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

# Password validation
@app.route('/validate-password', methods=['POST'])
def validate_password():
    data = request.get_json()
    if data.get('password') == FRONTEND_PASSWORD:
        return jsonify(success=True)
    return jsonify(success=False), 403

# Chat handler
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()
    if not user_message:
        return jsonify(error="Message is required"), 400

    if user_memory["name"] is None:
        match = re.search(r"(?:my name is|i am|i'm)\s+(\w+)", user_message, re.IGNORECASE)
        if match:
            user_memory["name"] = match.group(1).capitalize()

    system_prompt = (
        f"You are {user_memory['bot_name']}, a helpful AI assistant built by David Morris.\n"
        f"{'The user’s name is ' + user_memory['name'] + '.' if user_memory['name'] else ''}\n"
        "Speak like a real person, casually and clearly.\n"
        "You help with tech, life, coding, and creative ideas.\n"
    )

    conversation_history.append({"role": "user", "content": user_message})
    if len(conversation_history) > 20:
        conversation_history.pop(0)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": system_prompt}] + conversation_history
        )
        reply = response["choices"][0]["message"]["content"]
        conversation_history.append({"role": "assistant", "content": reply})
        return jsonify(reply=reply)
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
