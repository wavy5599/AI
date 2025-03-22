# Wavy'sBot 🌊🤖
Warning: You cannot access the chat bot unless you have the administrator password and server access 


This code is licensed under David Morris intellectual property


**Wavy’sBot** is a secure, full-stack AI chatbot powered by OpenAI’s GPT-4o model. It runs on a Flask backend and connects to a clean, responsive front-end interface where users can chat in real time — but only after passing a password gate. Password protection is securely handled through backend validation and stored privately using environment variables.

---

## 🔐 Features

- 🔒 Front-end password protection (user must unlock to chat)
- 🔐 Password and API securely stored in `.env`, never exposed to GitHub
- 🤖 AI responses from OpenAI’s GPT-4o
- 💬 Real-time frontend chat UI built in HTML/CSS/JS
- 🌐 CORS-enabled Flask server for clean frontend-backend communication
- 🧼 Repo is clean, safe, and production-ready

---

## 🧠 Tech Stack

- **Frontend:** HTML, CSS, JavaScript (vanilla)
- **Backend:** Python, Flask, Flask-CORS
- **AI:** OpenAI GPT-4o API
- **Security:** Environment variables, password validation via Flask

---

## 📂 Project Structure

```
WavysBot/
├── bot.py             # Flask server with OpenAI + password validation
├── index.html         # Frontend interface with chat and unlock logic
├── .env               # Secure config (not tracked)
├── .gitignore         # Ignores .env and config files
└── README.md          # You're here!
```

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/your-username/wavysbot.git
cd wavysbot
```

### 2. Create a `.env` file with your OpenAI API key and a password
```
key=your_openai_api_key_here
FRONTEND_PASSWORD=your_secure_password
```

### 3. Install Python dependencies
```bash
pip install flask flask-cors openai python-dotenv
```

### 4. Run the Flask server
```bash
python bot.py
```
Server will run at: `http://127.0.0.1:5000`

### 5. Open `index.html` with Live Server or manually in browser

---

## 🧪 How It Works
- User lands on the page and sees a password prompt
- Frontend sends password to `/validate-password`
- Flask compares against the `.env` password
- On success: frontend shows the chat interface
- User can now chat with the GPT-4o bot in real time

---

## 🛡 Security Notes

- ✅ Password is **never** exposed in the front end or pushed to GitHub
- ✅ `.env` is gitignored
- ❌ Do not hardcode passwords in `index.html`
- ✅ Password check is handled via Flask POST route

---

## 🧠 Built By

**Wavy** — a 19-year-old coder, builder, and visionary on a mission to level up and give back.

> “A nigga needed to hustle.” — Wavy

---

## 📈 Future Upgrades

- 🌍 Deploy backend to Render or Railway
- 🎙 Add voice input/output
- 🧠 Memory and chat logs
- 🧾 PDF exports of conversations
- 💳 Stripe integration for premium users

---

## 📸 Screenshots & Demo
_Add screenshots or a link to a demo here when ready!_

---

## 📜 License
MIT License
