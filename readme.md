<p align="center">
  <img src="./frontend/src/assets/Furia_Esports_logo.png" alt="Chatbot Furioso" width="150" /> <br />
  <b>Chatbot Furioso</b> <br />
  <sub><sup><b>(CHATBOT-FURIA V2)</b></sup></sub> <br />
</p>

<p align="center">
  Este projeto é um chatbot interativo desenvolvido para fornecer informações sobre o time de esports FURIA, o jogo Counter-Strike, campeonatos, partidas e muito mais. O chatbot agora utiliza RAG (Retrieval-Augmented Generation) e IA avançada para NLP, combinando React no frontend e Python + FastAPI no backend, integrando-se à API da PandaScore para obter dados em tempo real.
</p>

<p align="center">
  This project is an interactive chatbot designed to provide information about the FURIA esports team, the game Counter-Strike, tournaments, matches, and more. The chatbot now uses RAG (Retrieval-Augmented Generation) and advanced AI for NLP, combining React for the frontend and Python + FastAPI for the backend, integrating with the PandaScore API to fetch real-time data.
</p>

---

<details> <summary>🇧🇷 Detalhes do Projeto (Português)</summary>

## Resumo do Projeto

O **Chatbot Furioso V2** é uma aplicação web que permite aos usuários interagir com um chatbot para obter informações sobre o time FURIA Esports e o cenário competitivo de CS. Ele responde a perguntas sobre próximos jogos, resultados de partidas, estatísticas de jogadores, mapas, armas, campeonatos e muito mais. Agora, com a implementação de RAG e IA para NLP, o chatbot oferece respostas mais precisas e contextualizadas, utilizando um índice FAISS para recuperação de informações.

---

## Estrutura do Projeto

### Estrutura de Pastas

```
chatbot-furia  
├── backend  
│   ├── main.py  
│   ├── services/  
│   │   ├── populate_faiss.py  
│   │   └── faiss_retrieval.py  
│   ├── requirements.txt  
│   └── pycache/  
├── frontend  
│   ├── .gitignore  
│   ├── eslint.config.js  
│   ├── index.html  
│   ├── package.json  
│   ├── README.md  
│   ├── vite.config.js  
│   ├── public/  
│   │   └── vite.svg  
│   └── src/  
│       ├── App.css  
│       ├── App.jsx  
│       ├── index.css  
│       ├── main.jsx  
│       └── assets/  
│           ├── favicon/  
│           │   ├── favicon-32x32.png  
│           │   └── site.webmanifest  
│           └── ...  
└── venv/
```

---

### Backend

- **`main.py`**: Contém a API desenvolvida com FastAPI, responsável por fornecer dados ao chatbot.
- **`services/populate_faiss.py`**: Script para criar e popular o índice FAISS com dados relevantes.
- **`services/faiss_retrieval.py`**: Implementação do mecanismo de recuperação de informações utilizando FAISS e integração com o modelo de linguagem.
- **`requirements.txt`**: Lista de dependências do backend.

### Frontend

- **`App.jsx`**: Componente principal do chatbot, responsável pela interface e lógica de interação.
- **`index.html`**: Estrutura HTML principal do frontend.
- **`vite.config.js`**: Configuração do Vite para o projeto React.
- **`App.css` e `index.css`**: Estilos personalizados para o chatbot.

---

## Funcionalidades

- **Próximos Jogos**: Informações sobre as próximas partidas do time FURIA.
- **Últimos Resultados**: Resultados das partidas mais recentes da FURIA.
- **Lineup**: Lista de jogadores do time (especifique masculino ou feminino).
- **Estatísticas de Jogadores**: Dados como kills, deaths e ADR de jogadores específicos da FURIA.
- **Mapas**: Lista de mapas disponíveis no CS2.
- **Armas**: Informações sobre as armas do jogo.
- **Campeonatos**: Detalhes sobre campeonatos em andamento e futuros.
- **Sobre a FURIA**: Informações gerais sobre a organização FURIA Esports.
- **Respostas Contextualizadas**: Utiliza RAG para fornecer respostas baseadas em informações recuperadas do índice FAISS.
- **Integração com IA**: Respostas geradas por um modelo de linguagem avançado.

---

## Tecnologias e Ferramentas Utilizadas

### Frontend

- **React**: Biblioteca JavaScript para construção de interfaces de usuário.
- **Vite**: Ferramenta de build rápida para projetos frontend.
- **CSS**: Estilização da interface.

### Backend

- **FastAPI**: Framework para construção de APIs rápidas e performáticas.
- **Uvicorn**: Servidor ASGI para rodar a aplicação FastAPI.
- **Requests**: Biblioteca para realizar requisições HTTP.
- **FAISS**: Biblioteca para criação de índices vetoriais e recuperação de informações.
- **HuggingFace Transformers**: Para embeddings e geração de respostas.

### API Utilizada

- **PandaScore API**: API utilizada para obter dados sobre times, partidas, jogadores, mapas e campeonatos de CS2.

---

## Instruções de Uso

### Pré-requisitos

- Node.js e npm instalados para o frontend.
- Python 3.10+ instalado para o backend.

### Configuração do Backend

1. Navegue até a pasta `backend`:
   ```bash
   cd backend
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Crie o índice FAISS:
   ```bash
   python services/populate_faiss.py
   ```

4. Inicie o servidor:
   ```bash
   uvicorn main:app --reload
   ```

### Configuração do Frontend

1. Navegue até a pasta `frontend`:
   ```bash
   cd frontend
   ```

2. Instale as dependências:
   ```bash
   npm install
   ```

3. Inicie o Servidor de Desenvolvimento:
   ```bash
   npm run dev
   ```

---

### Acessando o Chatbot

- O frontend estará disponível em `http://localhost:5173`.
- O backend estará disponível em `http://localhost:8000`.

---

### Comandos Disponíveis

Aqui estão alguns exemplos de comandos que o chatbot entende:

- **Sobre a FURIA**: "Quem é a FURIA?"
- **Próximo Jogo**: "Qual o próximo jogo da FURIA?"
- **Últimos Resultados**: "Qual foi o último jogo da FURIA?"
- **Lineup**: "Quem está na lineup masculina da FURIA?"
- **Mapas**: "Quais são os mapas do CS?"
- **Armas**: "Quais são as armas do jogo?"
- **Próximas Partidas**: "Quais são as próximas partidas?"
- **Campeonatos Atuais**: "Quais campeonatos estão rolando?"
- **Campeonatos Futuros**: "Quais são os próximos campeonatos?"
- **Estatísticas de Jogadores**: "Quais são as estatísticas do jogador [nome]?"
- **Comandos**: "comandos" (lista todos os comandos disponíveis).

---

</details>

<details> <summary>🇺🇸 Project Details (English)</summary>

## Project Summary

The **Chatbot Furioso V2** is a web application that allows users to interact with a chatbot to get information about the FURIA Esports team and the competitive CS scene. It answers questions about upcoming games, match results, player statistics, maps, weapons, tournaments, and more. Now, with the implementation of RAG and AI for NLP, the chatbot provides more accurate and contextualized responses using a FAISS index for information retrieval.

---

## Project Structure

### Folder Structure

```
chatbot-furia  
├── backend  
│   ├── main.py  
│   ├── services/  
│   │   ├── populate_faiss.py  
│   │   └── faiss_retrieval.py  
│   ├── requirements.txt  
│   └── pycache/  
├── frontend  
│   ├── .gitignore  
│   ├── eslint.config.js  
│   ├── index.html  
│   ├── package.json  
│   ├── README.md  
│   ├── vite.config.js  
│   ├── public/  
│   │   └── vite.svg  
│   └── src/  
│       ├── App.css  
│       ├── App.jsx  
│       ├── index.css  
│       ├── main.jsx  
│       └── assets/  
│           ├── favicon/  
│           │   ├── favicon-32x32.png  
│           │   └── site.webmanifest  
│           └── ...  
└── venv/
```

---

### Backend

- **`main.py`**: Contains the API developed with FastAPI, responsible for providing data to the chatbot.
- **`services/populate_faiss.py`**: Script to create and populate the FAISS index with relevant data.
- **`services/faiss_retrieval.py`**: Implementation of the retrieval mechanism using FAISS and integration with the language model.
- **`requirements.txt`**: List of backend dependencies.

### Frontend

- **`App.jsx`**: Main component of the chatbot, responsible for the interface and interaction logic.
- **`index.html`**: Main HTML structure of the frontend.
- **`vite.config.js`**: Vite configuration for the React project.
- **`App.css` and `index.css`**: Custom styles for the chatbot.

---

## Features

- **Upcoming Games**: Information about FURIA's next matches.
- **Recent Results**: Results of FURIA's most recent matches.
- **Lineup**: List of team players (specify male or female).
- **Player Statistics**: Data such as kills, deaths, and ADR for specific FURIA players.
- **Maps**: List of available maps in CS2.
- **Weapons**: Information about the game's weapons.
- **Tournaments**: Details about ongoing and upcoming tournaments.
- **About FURIA**: General information about the FURIA Esports organization.
- **Contextualized Responses**: Uses RAG to provide answers based on information retrieved from the FAISS index.
- **AI Integration**: Responses generated by an advanced language model.

---

## Usage Instructions

### Prerequisites

- Node.js and npm installed for the frontend.
- Python 3.10+ installed for the backend.

### Backend Setup

1. Navigate to the `backend` folder:
   ```bash
   cd backend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create the FAISS index:
   ```bash
   python services/populate_faiss.py
   ```

4. Start the server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup

1. Navigate to the `frontend` folder:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the Development Server:
   ```bash
   npm run dev
   ```

---

### Accessing the Chatbot

- The frontend will be available at `http://localhost:5173`.
- The backend will be available at `http://localhost:8000`.

---

### Available Commands

Here are some examples of commands the chatbot understands:

- **About FURIA**: "Who is FURIA?"
- **Next Game**: "What is FURIA's next game?"
- **Recent Results**: "What was FURIA's last game?"
- **Lineup**: "Who is in FURIA's male lineup?"
- **Maps**: "What are the CS maps?"
- **Weapons**: "What are the weapons in the game?"
- **Upcoming Matches**: "What are the upcoming matches?"
- **Current Tournaments**: "What tournaments are happening?"
- **Future Tournaments**: "What are the next tournaments?"
- **Player Statistics**: "What are the stats for player [name]?"
- **Commands**: "commands" (lists all available commands).

[Watch the video showing the Chatbot working](https://drive.google.com/file/d/1VfLtNuTj5rxNgKKWLnjZJH7uc2ol3Ejk/view?usp=drive_link)

</details>

---

### License

This software is licensed under the terms of the MIT License.

---

<div align="center">

Developed by [Vitor Bittencourt](https://linktr.ee/vv_bittencourt) ☕

</div>