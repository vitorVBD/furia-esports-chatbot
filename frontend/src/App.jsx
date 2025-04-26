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

    const botReply = await getBotReply(userInput);
    setMessages((prev) => [...prev, { text: botReply, type: "bot" }]);
    setUserInput("");
  };

  const fetchData = async (url) => {
    try {
      const res = await fetch(url);
      return await res.json();
    } catch {
      return { error: "Erro na conexão com o servidor." };
    }
  };

  const getBotReply = async (inputRaw) => {
    const input = inputRaw.toLowerCase();

    switch (true) {
      case input.includes("próximo jogo"): {
        const data = await fetchData("http://localhost:8000/next-match");
        if (data.name) {
          return `🕹️ Próxima partida da FURIA: ${data.name}
🗓️ Data: ${new Date(data.start_date).toLocaleString()}
🆚 Adversário(s): ${data.location}`;
        }
        return data.message || "Não consegui encontrar a próxima partida.";
      }

      case input.includes("último jogo") ||
        input.includes("últimos resultados"): {
        const data = await fetchData("http://localhost:8000/last-match");
        if (data.match_name) {
          return `🎮 Último jogo:
${data.match_name}
📝 Resultado: ${data.result}
📅 Data: ${new Date(data.date).toLocaleString()}`;
        }
        return data.message || "Não consegui encontrar o último jogo.";
      }

      case input.includes("estatísticas") ||
        input.includes("kills") ||
        input.includes("adr"): {
        const playerName = input.split(" ")[1] || "";
        const data = await fetchData(
          `http://localhost:8000/player-stats?player_name=${playerName}`
        );
        if (data.player) {
          return `📊 Estatísticas de ${data.player}:
Kills: ${data.kills}
Deaths: ${data.deaths}
ADR: ${data.adr}`;
        }
        return (
          data.error || "Não consegui encontrar as estatísticas desse jogador."
        );
      }

      case input.includes("lineup") || input.includes("jogadores"): {
        const gender = input.includes("feminina") ? "feminino" : "masculino";
        const data = await fetchData(
          `http://localhost:8000/lineup?gender=${gender}`
        );
        if (data.lineup) {
          return `🎮 Lineup atual da FURIA (${gender}):\n- ${data.lineup.join(
            "\n- "
          )}`;
        }
        return data.error || "Não consegui encontrar a lineup.";
      }

      case input.includes("mapas") || input.includes("map"): {
        const data = await fetchData("http://localhost:8000/maps");
        if (data.maps) {
          return `🗺️ Lista de mapas do CS:\n- ${data.maps.join("\n- ")}`;
        }
        return data.error || "Não consegui encontrar os mapas.";
      }

      case input.includes("próximas partidas") ||
        input.includes("próximos jogos"): {
        const data = await fetchData(
          "http://localhost:8000/next-three-matches"
        );
        if (data.matches) {
          const formatted = data.matches.map((match) => {
        const date = new Date(match.date).toLocaleString("pt-BR", {
          dateStyle: "short",
          timeStyle: "short",
        });
        return `${match.opponents.join(" 🆚 ")}\n📅 Data: ${date} Horas`;
          });
          return `📅 Próximas três partidas:\n\n${formatted.join("\n\n")}`;
        }
        return data.error || "❌ Não consegui encontrar as partidas.";
      }

      case input.includes("campeonatos estão rolando") ||
        input.includes("campeonatos atuais"): {
        const data = await fetchData(
          "http://localhost:8000/current-tournaments"
        );
        if (data.tournaments) {
          const formatted = data.tournaments.map((t) => {
        const date = new Date(t.start_date).toLocaleDateString("pt-BR");
        return `🏆 ${t.name}\n   • Fase: ${t.stage}\n   • Iniciou em: ${date}`;
          });
          return `Campeonatos em andamento:\n\n${formatted.join("\n\n")}`;
        }
        return data.error || "Não consegui encontrar campeonatos em andamento.";
      }

      case input.includes("campeonatos futuros") ||
        input.includes("próximos campeonatos"): {
        const data = await fetchData(
          "http://localhost:8000/upcoming-tournaments"
        );
        if (data.tournaments) {
          const formatted = data.tournaments.map((t) => {
            const date = new Date(t.start_date).toLocaleDateString("pt-BR");
            return `🏆 ${t.name}\n   • ${t.stage}\n   • 📆 começa em: ${date})`;
          });
          return `Próximos campeonatos:\n\n ${formatted.join("\n\n")}`;
        }
        return data.error || "Não encontrei campeonatos futuros.";
      }

      case input.includes("armas do jogo") ||
        input.includes("todas as armas") ||
        input.includes("armas do cs"): {
        const data = await fetchData("http://localhost:8000/game-weapons");
        if (data.weapons) {
          return `🔫 Armas disponíveis no jogo:\n\n${data.weapons
            .slice(0, 5)
            .map((w) => `• ${w.name} (${w.kind})`)
            .join("\n\n")}`;
        }
        return data.error || "Não consegui encontrar as armas.";
      }

      case input.includes("furia") || input.includes("sobre a furia"): {
        return `A FURIA Esports é uma organização brasileira de esports fundada em 2017 por André Akkari, Jaime Pádua e Cris Guedes. Inicialmente focada em Counter-Strike: Global Offensive (CS:GO), a FURIA expandiu para diversas outras modalidades, como Rocket League, League of Legends, Valorant, Rainbow Six: Siege e Apex Legends. A organização é conhecida por sua forte presença no cenário competitivo e pela sua popularidade entre os fãs de esports.`;
      }

      case input.includes("comandos") || input.includes("lista de comandos"): {
        return `Aqui estão alguns comandos que você pode usar:
        
- 'Sobre a FURIA'
- 'Qual o próximo jogo da FURIA?'
- 'Qual foi o último jogo da FURIA?'
- 'Quem está na lineup masculina ou feminina da FURIA?'
- 'Quais são os mapas do CS?'
- 'Quais são as armas do jogo?'
- 'Quais são as próximas partidas?'
- 'Quais são os próximos campeonatos?'
- 'Quais campeonatos estão rolando?'
- 'Quais são as estatísticas do jogador [nome]?'`;
      }

      default:
        return "Ainda não entendi sua pergunta 😅 \n Digite 'comandos' para ver a lista completa de comandos";
    }
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
      <footer className="footer">
      Desenvolvido por Vitor Bittencourt
    </footer>
    </div>
  );
}

export default App;
