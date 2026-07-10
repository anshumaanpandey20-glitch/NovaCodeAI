document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("chatForm");
    const input = document.getElementById("messageInput");
    const chatBox = document.getElementById("chatBox");

    if (!form || !input || !chatBox) return;

    const appendMessage = (text, role = "assistant") => {
        const msg = document.createElement("div");
        msg.textContent = `${role === "assistant" ? "Assistant" : "You"}: ${text}`;
        chatBox.appendChild(msg);
    };

    form.addEventListener("submit", (e) => {
        e.preventDefault();
        const message = input.value.trim();
        if (!message) return;

        appendMessage(message, "user");
        input.value = "";
        appendMessage(`Echo: ${message}`);
    });
});
