async function unlockChat() {
    const password = document.getElementById('accessPassword').value;

    const res = await fetch("http://127.0.0.1:5000/validate-password", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ password })
    });

    const data = await res.json();
    if (data.success) {
      document.getElementById('authBox').style.display = 'none';
      document.getElementById('chatBox').style.display = 'block';
    } else {
      alert("Incorrect password.");
    }
  }

  async function sendMessage() {
    const input = document.getElementById('userInput');
    const chatLog = document.getElementById('chatLog');
    const userMessage = input.value;

    if (!userMessage.trim()) return;

    const userDiv = document.createElement('div');
    userDiv.className = 'message user';
    userDiv.innerText = userMessage;
    chatLog.appendChild(userDiv);

    try {
      const response = await fetch('http://127.0.0.1:5000/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userMessage })
      });

      const data = await response.json();
      const botReply = data.reply || "Error: " + data.error;

      const botDiv = document.createElement('div');
      botDiv.className = 'message bot';
      botDiv.innerText = botReply;
      chatLog.appendChild(botDiv);

      input.value = '';
      chatLog.scrollTop = chatLog.scrollHeight;
    } catch (error) {
      console.error('Error:', error);
    }
  }

  document.getElementById("userInput").addEventListener("keyup", function (event) {
    if (event.key === "Enter") {
      sendMessage();
    }
  });