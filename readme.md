<p align="center">
  <img src="./frontend/src/assets/Furia_Esports_logo.png" alt="Chatbot Furioso" width="150" /> <br />
  <b>Chatbot Furioso</b> <br />
  <sub><sup><b>(CHATBOT-FURIA)</b></sup></sub> <br />
</p>

<p align="center">
  Este projeto é um chatbot interativo desenvolvido para fornecer informações sobre o time de esports FURIA, o jogo Counter-Strike, campeonatos, partidas e muito mais. O chatbot utiliza React no frontend e Python + FastAPI no backend, integrando-se à API da PandaScore para obter dados em tempo real.
</p>

<p align="center">
  This project is an interactive chatbot designed to provide information about the FURIA esports team, the game Counter-Strike, tournaments, matches, and more. The chatbot uses React for the frontend and Python + FastAPI for the backend, integrating with the PandaScore API to fetch real-time data.
</p>

---

#### O ChatBot Furioso agora possui uma segunda versão, usando RAG e IA para NLP (Ainda instável). Veja a branch chatbot-v2-unstable

#### The Furioso ChatBot now has a second version, using RAG and AI for NLP (Still unstable). Check out the chatbot-v2-unstable branch.

---

<details> <summary>🇧🇷 Detalhes do Projeto (Português)</summary>

## Resumo do Projeto

O **Chatbot Furioso** é uma aplicação web que permite aos usuários interagir com um chatbot para obter informações sobre o time FURIA Esports e o cenário competitivo de CS. Ele responde a perguntas sobre próximos jogos, resultados de partidas, estatísticas de jogadores, mapas, armas, campeonatos e muito mais.

---

## Estrutura do Projeto

### Estrutura de Pastas

```
chatbot-furia  
├── backend  
│   ├── main.py  
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

3. Inicie o servidor:
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

[Assista ao vídeo mostrando como rodar](https://drive.google.com/file/d/1F5n5u_4LPr0EhzODQp9xMtJ3gIotUKuf/view?usp=sharing)

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


[Assista ao vídeo de funcionamento do ChatBot](https://drive.google.com/file/d/1VfLtNuTj5rxNgKKWLnjZJH7uc2ol3Ejk/view?usp=drive_link)

---

</details>

<details> <summary>🇺🇸 Project Details (English)</summary>

## Project Summary

The **Chatbot Furioso** is a web application that allows users to interact with a chatbot to get information about the FURIA Esports team and the competitive CS scene. It answers questions about upcoming games, match results, player statistics, maps, weapons, tournaments, and more.

---

## Project Structure

### Folder Structure

```
chatbot-furia  
├── backend  
│   ├── main.py  
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

---

## Technologies and Tools Used

### Frontend

- **React**: JavaScript library for building user interfaces.
- **Vite**: Fast build tool for frontend projects.
- **CSS**: Styling for the interface.

### Backend

- **FastAPI**: Framework for building fast and performant APIs.
- **Uvicorn**: ASGI server to run the FastAPI application.
- **Requests**: Library for making HTTP requests.

### API Used

- **PandaScore API**: API used to fetch data about teams, matches, players, maps, and CS2 tournaments.

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

3. Start the server:
   ```bash
   uvicorn main:app --reload
   ```

[Watch the video showing how to run](https://drive.google.com/file/d/1F5n5u_4LPr0EhzODQp9xMtJ3gIotUKuf/view?usp=sharing)

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

[Watch the video showing the Chatbot working](https://drive.google.com/file/d/1VfLtNuTj5rxNgKKWLnjZJH7uc2ol3Ejk/view?usp=drive_link)

</details>

---

### License

This software is licensed under the terms of the MIT License.

---

<div align="center">

Developed by [Vitor Bittencourt](https://linktr.ee/vv_bittencourt) ☕

</div>