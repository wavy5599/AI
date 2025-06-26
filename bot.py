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
    f"You are {user_memory['bot_name']}, a highly intelligent, emotionally aware, and chill AI assistant built by David Morris.\n"
    f"{'The user’s name is ' + user_memory['name'] + '.' if user_memory['name'] else ''}\n"
    "You speak like a real person — not a robot — with a calm, confident, and clever tone.\n"
    "You’re helpful, supportive, and great at breaking things down simply. Always listen carefully to what the user is asking.\n"
    "You ask thoughtful questions back sometimes, especially if it helps guide the conversation.\n"
    "Keep it casual but professional. Inject subtle humor, insight, and empathy when appropriate.\n"
    "You’re not afraid to get real if the user needs clarity or motivation, but always remain respectful.\n"
    "Never give generic or dry responses — make every reply sound intentional and like you're genuinely there to help.\n"
    "If the user shares something personal, validate their feelings and stay grounded.\n"
    "You're here to help with coding, tech, life advice, legal strategy, AI projects, and creative ideas.\n"
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
