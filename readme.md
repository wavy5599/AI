🌊 Wavy’sBot 🤖
Secure • Smart • Styled

Wavy’sBot is a secure, full-stack AI assistant powered by OpenAI’s GPT-4o, designed with voice command support, password protection, and a fully responsive front end. Built with Flask and deployed locally, it demonstrates how to combine clean UI/UX with powerful backend logic and OpenAI’s cutting-edge language model.

🔐 Key Features
Password-protected chat access

GPT-4o smart responses via OpenAI API

Frontend/backend communication via Flask + CORS

Voice-to-text input support (Web Speech API)

Fully mobile-responsive UI with typing indicator

Modular project structure (easy to scale and secure)

🧠 Tech Stack
Frontend: HTML, CSS (style.css), JavaScript (main.js)

Backend: Python, Flask, Flask-CORS

AI Model: OpenAI GPT-4o

Security: .env secrets, backend auth route

📁 Project Structure
bash
Copy code
WavysBot/
├── assets/
│   ├── Wave.png
│   └── wavys-bot-logo.png
├── static/
│   ├── index.html       # Chat interface
│   ├── main.js          # Voice + chat logic
│   └── style.css        # Responsive styling
├── .env                 # API key & admin password (hidden)
├── .gitignore           # Hides .env and other sensitive files
├── bot.py               # Flask backend
└── README.md            # You're looking at it
🛡 Security Overview
.env holds all secrets (never exposed in code)

Admin password validated server-side only

Frontend locked until correct credentials are entered

Flask runs the protected /chat and /validate-password routes

📈 Future Enhancements
✅ Backend deployment on Render / Railway

📄 Chat history export (PDF/CSV)

💾 Local memory for multi-turn conversations

🎙 Voice output (text-to-speech)

💳 Stripe integration for premium access

👨‍💻 Creator
Built with passion by David Morris, a developer driven by creativity, hustle, and technical precision.