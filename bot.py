# 📦 Import required libraries
import openai                   # For interacting with the OpenAI API
import os                       # To work with environment variables like your API key
from dotenv import load_dotenv # To load environment variables from a .env file
from flask import Flask, request, jsonify  # Flask for the web server
from flask_cors import CORS    # CORS to allow frontend apps to connect to this backend

#  Load environment variables from the .env file (API key, frontend password, etc.)
load_dotenv()

#  Initialize the Flask app
app = Flask(__name__)

#  Enable Cross-Origin Resource Sharing (CORS) so your frontend can call this API from a different domain
CORS(app)

#  Get the OpenAI API key and frontend password from environment variables
openai.api_key = os.getenv('key')
FRONTEND_PASSWORD = os.getenv('FRONTEND_PASSWORD')
guest_key = os.getenv('guest_key')

#  Route: Root endpoint to confirm server is running
@app.route('/')
def home():
    return "Flask server with AI Chatbot is running!"  # Simple response for testing

#  Route: Validate frontend password to make sure only approved users can access
@app.route('/validate-password', methods=['POST'])
def validate_password():
    data = request.get_json()  # Get JSON payload from frontend
    submitted_password = data.get('password')  # Extract submitted password
    if submitted_password == FRONTEND_PASSWORD:  # Compare with the correct one
        return jsonify({"success": True})        # Password is correct
    else:
        return jsonify({"success": False}), 403  # Wrong password, return error

#  Route: Handle chat requests from the frontend
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()             # Get JSON payload from frontend
    user_message = data.get("message")    # Extract the message sent by the user

    #  Error handling: If there's no message in the request
    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    try:
        #  Call OpenAI's ChatCompletion API with GPT-4o model
        response = openai.ChatCompletion.create(
            model="gpt-4o",  # GPT-4o (Omni model)
            messages=[{"role": "user", "content": user_message}]
        )

        #  Extract AI's reply from the response
        bot_reply = response["choices"][0]["message"]["content"]

        #  Send AI's reply back to the frontend
        return jsonify({"reply": bot_reply})

    except Exception as e:
        #  If something goes wrong (like API error), return the error message
        return jsonify({"error": str(e)}), 500

#  Start the Flask server when this script is run directly
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Run on port 5000, open to all network interfaces
