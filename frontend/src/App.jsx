import React, { useState, useRef, useEffect } from "react";

function App() {
  const [messages, setMessages] = useState([
    { text: "Bem vindo ao chatbot FURIOSO! \n\n (Digite 'comandos' para listar os comandos)", type: "bot" },
  ]);
  const [userInput, setUserInput] = useState("");
  const messagesEndRef = useRef(null);
  
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);
  
  const handleSend = async () => {
    if (!userInput.trim()) return;

    const userMessage = { text: userInput, type: "user" };
    setMessages((prev) => [...prev, userMessage]);

    try {
      const response = await fetch("http://localhost:8000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: userInput }), // Certifique-se de usar "question"
      });
      const data = await response.json();
      const botReply = data.answer || "Desculpe, não consegui encontrar uma resposta.";
      setMessages((prev) => [...prev, { text: botReply, type: "bot" }]);
    } catch {
      setMessages((prev) => [...prev, { text: "Erro ao se conectar ao servidor.", type: "bot" }]);
    }

    setUserInput("");
  };

  return (
    <div className="chat-container">
      <div className="chat-box">
        {messages.map((message, index) => (
          <div
            key={index}
            className={message.type === "bot" ? "bot-message" : "user-message"}
          >
            {message.text}
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>
      <input
        type="text"
        value={userInput}
        onChange={(e) => setUserInput(e.target.value)}
        placeholder="Pergunte sobre CS ou sobre a FURIA..."
        onKeyDown={(e) => e.key === "Enter" && handleSend()}
      />
      <button onClick={handleSend}>Enviar</button>
      <footer className="footer">Desenvolvido por Vitor Bittencourt</footer>
    </div>
  );
}

export default App;