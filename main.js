const SERVER_URL = "http://192.168.1.206:5000"; // Your backend
let username = "";

// 🔗 Get elements
const micButton = document.getElementById("micButton");
const userInput = document.getElementById("userInput");
const sendButton = document.getElementById("sendButton");
const unlockButton = document.getElementById("unlockButton");
const chatLog = document.getElementById("chatLog");

// 🧠 Event listeners
sendButton.addEventListener("click", sendMessage);
unlockButton.addEventListener("click", unlockChat);

// ✅ Append messages
function appendMessage(sender, text) {
  const message = document.createElement("div");
  message.className = `message ${sender === "user" ? "user" : "bot"}`;
  message.innerHTML = `<strong>${sender === "user" ? "You" : "Bot"}:</strong> ${text}`;
  chatLog.appendChild(message);
  chatLog.scrollTop = chatLog.scrollHeight;
}

function appendTyping() {
  const typing = document.createElement("div");
  typing.className = "message bot";
  typing.id = "typing";
  typing.innerHTML = `<strong>Bot:</strong> <span class='typing-dots'><span></span><span></span><span></span></span>`;
  chatLog.appendChild(typing);
  chatLog.scrollTop = chatLog.scrollHeight;
}

function removeTyping() {
  const typing = document.getElementById("typing");
  if (typing) typing.remove();
}

// 🔐 Unlock chat
async function unlockChat() {
  const password = document.getElementById("accessPassword").value;
  const authBox = document.getElementById("authBox");
  const chatBox = document.getElementById("chatBox");

  try {
    const res = await fetch(`${SERVER_URL}/validate-password`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ password })
    });
    const data = await res.json();

    if (data.success) {
      authBox.style.display = "none";
      chatBox.style.display = "block";
      appendMessage("bot", "Welcome! What's your name?");
    } else {
      alert("Incorrect password. Try again.");
    }
  } catch (err) {
    alert("Server error. Try again later.");
  }
}

// 📤 Send user message
async function sendMessage() {
  const message = userInput.value.trim();
  if (!message) return;

  appendMessage("user", message);
  userInput.value = "";

  if (!username) {
    username = message;
    appendMessage("bot", `Nice to meet you, ${username}. How can I help you today?`);
    return;
  }

  appendTyping();

  try {
    const res = await fetch(`${SERVER_URL}/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message })
    });
    const data = await res.json();
    removeTyping();
    appendMessage("bot", data.reply);
  } catch (err) {
    removeTyping();
    appendMessage("bot", "Oops! Something went wrong.");
  }
}

// 🎤 Mic Integration (Fills input box with spoken text)
let isListening = false;
let recognition;

if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  recognition = new SpeechRecognition();

  recognition.continuous = true; // 🔥 Keep listening
  recognition.interimResults = false;
  recognition.lang = 'en-US';

  micButton.addEventListener("click", () => {
    if (isListening) {
      recognition.stop();
      micButton.innerText = "🎤";
      isListening = false;
    } else {
      recognition.start();
      micButton.innerText = "🛑 Stop Listening";
      isListening = true;
    }
  });

  recognition.onresult = (event) => {
    const transcript = event.results[event.results.length - 1][0].transcript;
    userInput.value = transcript;
    userInput.focus();
  };

  recognition.onerror = (event) => {
    console.error("Speech recognition error:", event.error);
    micButton.innerText = "🎤";
    isListening = false;
  };

  recognition.onend = () => {
    if (isListening) {
      recognition.start(); // 🔁 Auto-restart if accidentally ended
    }
  };
} else {
  micButton.disabled = true;
  micButton.title = "Speech recognition not supported in this browser";
}

