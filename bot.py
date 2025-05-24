import openai
import os
import re
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS

# 🌱 Load environment variables
load_dotenv()

# 🚀 Initialize Flask app
app = Flask(__name__)
CORS(app)

# 🔐 API Keys
openai.api_key = os.getenv('key')
FRONTEND_PASSWORD = os.getenv('FRONTEND_PASSWORD')
guest_key = os.getenv('guest_key')

# 🧠 In-memory session state
user_memory = {
    "name": None,
    "bot_name": "Wavy's Bot"
}
conversation_history = []

# ✅ Home route
@app.route('/')
def home():
    return "Flask server with AI Chatbot is running!"

# 🔑 Password validation
@app.route('/validate-password', methods=['POST'])
def validate_password():
    data = request.get_json()
    if data.get('password') == FRONTEND_PASSWORD:
        return jsonify(success=True)
    return jsonify(success=False), 403

# 🤖 Chat route
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify(error="Message is required"), 400

    # 🔍 Detect and save user name if not known
    if user_memory["name"] is None:
        match = re.search(r"(?:my name is|i am|i'm)\s+(\w+)", user_message, re.IGNORECASE)
        if match:
            user_memory["name"] = match.group(1).capitalize()

    # 🧠 System prompt
    system_prompt = (
        f"You are {user_memory['bot_name']}, a helpful, chill, and clever AI assistant who sounds like a real person.\n"
        f"{'The user’s name is ' + user_memory['name'] + '.' if user_memory['name'] else ''}\n"
        "Use friendly tone, ask questions back sometimes, and be supportive. Don't sound robotic."
    )

    # 🗃️ Maintain session memory
    conversation_history.append({"role": "user", "content": user_message})
    if len(conversation_history) > 20:
        conversation_history.pop(0)  # Limit memory size

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

# 🔥 Run server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
