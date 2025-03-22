# Wavy'sBot 🌊🤖

> ⚠️ **Warning:** Access to this chatbot requires administrator permission and an active server connection.

> 🧠 **Protected By:** David Morris Intellectual Property. Unauthorized use, reproduction, or distribution is strictly prohibited.

**Wavy’sBot** is a secure, full-stack AI chatbot that leverages OpenAI’s GPT-4o model to generate intelligent and responsive conversations. Built with a password-gated front-end and Flask-powered backend, this project ensures only authorized users can interact with the chatbot.

---

## 🔐 Features

- 🔒 Password-protected chat access
- 🧠 GPT-4o responses via OpenAI API
- 🔐 Secure credential storage in `.env` (never exposed)
- 🌐 Flask backend with CORS for smooth frontend integration
- 🎨 Styled and responsive UI built with HTML, CSS, and JavaScript

---

## 🧠 Tech Stack

- **Frontend:** HTML, CSS (`styles.css`), JavaScript (`server.js`)
- **Backend:** Python, Flask, Flask-CORS
- **AI Model:** OpenAI GPT-4o
- **Security:** Environment variables & server-side validation

---

## 📁 File Structure

```
WavysBot/
├── bot.py           # Flask backend API
├── index.html       # Main HTML file with chat interface
├── styles.css       # UI styling for chat
├── server.js        # Front-end JS logic (password + chat)
├── .env             # API keys & admin password (excluded)
├── .gitignore       # Excludes .env and sensitive files
└── README.md        # Project overview
```

---

## 🛡 Security Overview

- 🔐 `.env` file securely stores API keys and passwords
- ❌ No credentials are exposed in public files
- ✅ Password check is handled via a backend validation route
- 🔒 Server must be running for chat to function

---

## 📈 Planned Enhancements

- 🌐 Backend deployment on Render/Railway
- 🧠 Persistent chat memory & log history
- 🧾 Export chat to PDF
- 🔊 Voice input/output integration
- 💳 Premium access via Stripe

---

## 👨‍💻 Built By

**David Morris (Wavy)** — young visionary, innovator, and builder on a mission to protect his mind, his grind, and his code.

> “A nigga needed to hustle.” — Wavy

---

## 📸 Demo & Screenshots
_Add media or demo link here when ready._

---

## 📜 License
MIT License — Custom implementations and system design remain the Intellectual Property of **David Morris**.
