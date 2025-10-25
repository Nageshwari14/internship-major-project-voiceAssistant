const sendBtn = document.getElementById("send-btn");
const micBtn = document.getElementById("mic-btn");
const userInput = document.getElementById("user-input");
const chatBox = document.getElementById("chat-box");

const backendURL = "http://127.0.0.1:5000/command";

// Load chat history from localStorage
let chatHistory = JSON.parse(localStorage.getItem("chatHistory")) || [];

function renderChat() {
    chatBox.innerHTML = "";
    chatHistory.forEach(item => appendMessage(item.sender, item.text, false));
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Append message and save to history
function appendMessage(sender, text, save=true) {
    const msg = document.createElement("div");
    msg.classList.add("message", sender);
    msg.textContent = text;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;

    if(save) {
        chatHistory.push({sender, text});
        localStorage.setItem("chatHistory", JSON.stringify(chatHistory));
    }
}

async function sendMessage(message) {
    if (!message.trim()) return;
    appendMessage("user", message);

    userInput.value = "";

    try {
        const res = await fetch(backendURL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ command: message })
        });
        const data = await res.json();
        appendMessage("bot", data.response);
        speakResponse(data.response);
    } catch (err) {
        appendMessage("bot", "Couldn't connect to backend.");
    }
}

sendBtn.addEventListener("click", () => sendMessage(userInput.value));
userInput.addEventListener("keypress", e => { if(e.key === "Enter") sendMessage(userInput.value); });

function speakResponse(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = "en-US";
    window.speechSynthesis.speak(utterance);
}

// Voice recognition with mic glow
micBtn.addEventListener("click", () => {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) {
        appendMessage("bot", "Browser does not support voice recognition.");
        return;
    }

    micBtn.classList.add("mic-listening");

    const recognition = new SpeechRecognition();
    recognition.lang = "en-US";
    recognition.interimResults = false;
    recognition.continuous = false;

    recognition.start();

    recognition.onresult = event => {
        const transcript = event.results[0][0].transcript;
        sendMessage(transcript);
        micBtn.classList.remove("mic-listening");
    };

    recognition.onerror = () => {
        appendMessage("bot", "Could not hear you. Try again.");
        micBtn.classList.remove("mic-listening");
    };

    recognition.onend = () => {
        micBtn.classList.remove("mic-listening");
    };
});

// Render chat on page load
renderChat();












