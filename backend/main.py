from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from services.faiss_retrieval import initialize_retrieval_qa
import requests

API_KEY = "VyuJGyw9ejTo66QJLPuD5eRsXVTiR3302URgCmKNzwpnMZN3j48"
headers = {"Authorization": f"Bearer {API_KEY}"}

app = FastAPI()

# Libera acesso do React (frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # porta padrão do Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo para validar o corpo da requisição
class QuestionRequest(BaseModel):
    question: str

qa_chain = initialize_retrieval_qa()

@app.post("/ask")
def ask_question(request: QuestionRequest):
    try:
        # Verifica se o comando é "comandos"
        if request.question.lower() == "comandos":
            return {
                "answer": (
                    "Comandos disponíveis:\n"
                    "- 'próximo jogo': Informa o próximo jogo da FURIA.\n"
                    "- 'lineup masculina': Mostra a lineup masculina da FURIA.\n"
                    "- 'último jogo': Mostra informações sobre o último jogo.\n"
                    "- 'estatísticas': Mostra estatísticas de um jogador.\n"
                    "- 'mapas': Lista os mapas disponíveis.\n"
                    "- 'próximos três jogos': Lista os próximos três jogos.\n"
                    "- 'torneios atuais': Lista os torneios em andamento.\n"
                    "- 'próximos torneios': Lista os próximos torneios.\n"
                    "- 'armas': Lista as armas disponíveis no jogo."
                )
            }

        # Verifica se o comando é "lineup masculina"
        if request.question.lower() == "lineup masculina":
            response = requests.get("http://127.0.0.1:8000/lineup?gender=masculino")
            lineup_data = response.json()

            if "lineup" in lineup_data:
                context = f"A lineup masculina da FURIA é composta pelos seguintes jogadores: {', '.join(lineup_data['lineup'])}."
            else:
                context = lineup_data.get("error", "Não foi possível obter a lineup masculina da FURIA.")

            llm_response = qa_chain.run(f"Pergunta: {request.question}. Contexto: {context}")
            return {"answer": llm_response}
        
        # Verifica se o comando é "lineup masculina"
        if request.question.lower() == "lineup feminina":
            response = requests.get("http://127.0.0.1:8000/lineup?gender=feminino")
            lineup_data = response.json()

            if "lineup" in lineup_data:
                context = f"A lineup feminina da FURIA é composta pelos seguintes jogadores: {', '.join(lineup_data['lineup'])}."
            else:
                context = lineup_data.get("error", "Não foi possível obter a lineup feminina da FURIA.")

            llm_response = qa_chain.run(f"Pergunta: {request.question}. Contexto: {context}")
            return {"answer": llm_response}

        # Verifica se o comando é "último jogo"
        if request.question.lower() == "último jogo":
            response = requests.get("http://127.0.0.1:8000/last-match")
            match_data = response.json()

            if "last_match" in match_data:
                context = f"O último jogo da FURIA foi: {match_data['last_match']}."
            else:
                context = match_data.get("error", "Não foi possível obter informações sobre o último jogo.")

            llm_response = qa_chain.run(f"{request.question}. Contexto: {context}")
            return {"answer": llm_response}

        # Verifica se o comando é "estatísticas"
        if request.question.lower().startswith("estatísticas"):
            player_name = request.question.split("estatísticas de")[-1].strip()
            response = requests.get(f"http://127.0.0.1:8000/player-stats?player_name={player_name}")
            stats_data = response.json()

            if "player" in stats_data:
                context = (
                    f"Estatísticas de {stats_data['player']}:\n"
                    f"Kills: {stats_data['kills']}, Deaths: {stats_data['deaths']}, ADR: {stats_data['adr']}."
                )
            else:
                context = stats_data.get("error", f"Não foi possível obter estatísticas para {player_name}.")

            llm_response = qa_chain.run(f"{request.question}. Contexto: {context}")
            return {"answer": llm_response}

        # Verifica se o comando é "mapas"
        if request.question.lower() == "mapas":
            response = requests.get("http://127.0.0.1:8000/maps")
            maps_data = response.json()

            if "maps" in maps_data:
                context = f"Os mapas disponíveis no jogo são: {', '.join(maps_data['maps'])}."
            else:
                context = maps_data.get("error", "Não foi possível obter os mapas disponíveis.")

            # Passa o contexto para o LLM
            llm_response = qa_chain.run(f"Pergunta: {request.question}. Contexto: {context}")
            return {"answer": llm_response}

        # Verifica se o comando é "próximos três jogos"
        if request.question.lower() == "próximos três jogos":
            response = requests.get("http://127.0.0.1:8000/next-three-matches")
            matches_data = response.json()

            if "matches" in matches_data:
                context = "Os próximos três jogos da FURIA são:\n" + "\n".join(
                    [f"{match['name']} - {match['date']}" for match in matches_data["matches"]]
                )
            else:
                context = matches_data.get("error", "Não foi possível obter informações sobre os próximos jogos.")

            llm_response = qa_chain.run(f"{request.question}. Contexto: {context}")
            return {"answer": llm_response}

        # Verifica se o comando é "torneios atuais"
        if request.question.lower() == "torneios atuais":
            response = requests.get("http://127.0.0.1:8000/current-tournaments")
            tournaments_data = response.json()

            if "tournaments" in tournaments_data:
                context = "Os torneios em andamento são:\n" + "\n".join(
                    [f"{tournament['name']} - {tournament['stage']}" for tournament in tournaments_data["tournaments"]]
                )
            else:
                context = tournaments_data.get("error", "Não foi possível obter informações sobre os torneios atuais.")

            llm_response = qa_chain.run(f"{request.question}. Contexto: {context}")
            return {"answer": llm_response}

        # Verifica se o comando é "próximos torneios"
        if request.question.lower() == "próximos torneios":
            response = requests.get("http://127.0.0.1:8000/upcoming-tournaments")
            tournaments_data = response.json()

            if "tournaments" in tournaments_data:
                context = "Os próximos torneios são:\n" + "\n".join(
                    [f"{tournament['name']} - {tournament['start_date']}" for tournament in tournaments_data["tournaments"]]
                )
            else:
                context = tournaments_data.get("error", "Não foi possível obter informações sobre os próximos torneios.")

            llm_response = qa_chain.run(f"{request.question}. Contexto: {context}")
            return {"answer": llm_response}

        # Verifica se o comando é "armas"
        if request.question.lower() == "armas":
            response = requests.get("http://127.0.0.1:8000/game-weapons")
            weapons_data = response.json()

            if "weapons" in weapons_data:
                context = "As armas disponíveis no jogo são:\n" + "\n".join(
                    [f"{weapon['name']} ({weapon['kind']})" for weapon in weapons_data["weapons"]]
                )
            else:
                context = weapons_data.get("error", "Não foi possível obter informações sobre as armas.")

            llm_response = qa_chain.run(f"{request.question}. Contexto: {context}")
            return {"answer": llm_response}

        # Caso contrário, processa a pergunta normalmente
        response = qa_chain.run(request.question)
        return {"answer": response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/lineup")
def get_lineup(gender: str = "masculino"):
    teams = requests.get(
        "https://api.pandascore.co/csgo/teams",
        headers=headers,
        params={"search[name]": "FURIA"}
    ).json()

    if not teams:
        return {"error": "FURIA não encontrada"}

    # Filtrar pelo gênero
    if gender == "masculino":
        team = next((t for t in teams if t.get("acronym") == "FURIA" and not t["name"].lower().endswith("fe")), None)
    elif gender == "feminino":
        team = next((t for t in teams if "fe" in t["name"].lower()), None)
    else:
        return {"error": "Gênero inválido. Use masculino ou feminino."}

    if not team:
        return {"error": f"Time {gender} da FURIA não encontrado"}

    players = team.get("players", [])
    lineup = [player["name"] or player["first_name"] for player in players]

    return {"lineup": lineup, "team_name": team["name"]}

@app.get("/player-stats")
def player_stats(player_name: str, gender: str = "masculino"):
    teams = requests.get(
        "https://api.pandascore.co/csgo/teams",
        headers=headers,
        params={"search[name]": "FURIA"}
    ).json()

    if not teams:
        return {"error": "FURIA não encontrada"}

    if gender == "masculino":
        team = next((t for t in teams if t.get("acronym") == "FURIA" and not t["name"].lower().endswith("fe")), None)
    elif gender == "feminino":
        team = next((t for t in teams if "fe" in t["name"].lower()), None)
    else:
        return {"error": "Gênero inválido. Use masculino ou feminino."}

    if not team:
        return {"error": f"Time {gender} da FURIA não encontrado"}

    player = next((p for p in team.get("players", []) if player_name.lower() in p["name"].lower()), None)
    if not player:
        return {"error": f"Jogador {player_name} não encontrado no time {team['name']}."}

    stats = player.get("stats", {})
    return {
        "player": player["name"],
        "kills": stats.get("kills", "N/A"),
        "deaths": stats.get("deaths", "N/A"),
        "adr": stats.get("adr", "N/A"),
    }

@app.get("/maps")
def get_maps():
    response = requests.get(
        "https://api.pandascore.co/csgo/maps",
        headers=headers
    )
    maps = response.json()

    if not maps:
        return {"error": "Nenhum mapa encontrado."}

    map_names = [map["name"] for map in maps]
    return {"maps": map_names}

@app.get("/next-three-matches")
def next_all_matches():
    response = requests.get(
        "https://api.pandascore.co/csgo/matches/upcoming", 
        headers=headers
    )
    matches = response.json()

    if not matches:
        return {"error": "Nenhuma partida futura encontrada."}

    match_list = []
    for match in matches[:3]:  # Pegando as 3 primeiras partidas
        # Verificando se o campo "opponents" está presente
        if "opponents" in match:
            match_info = {
                "name": match["name"],
                "date": match["begin_at"],
                "opponents": [op["opponent"]["name"] for op in match["opponents"]]
            }
            match_list.append(match_info)

    return {"matches": match_list}

@app.get("/current-tournaments")
def running_tournaments():
    response = requests.get(
        "https://api.pandascore.co/csgo/tournaments/running",
        headers=headers
    )
    tournaments = response.json()

    if not tournaments:
        return {"error": "Nenhum campeonato em andamento encontrado."}

    tournament_list = []
    for tournament in tournaments:
        tournament_info = {
            "name": tournament["serie"]["full_name"] if tournament.get("serie") else tournament["name"],
            "stage": tournament["name"],
            "start_date": tournament["begin_at"]
        }
        tournament_list.append(tournament_info)

    return {"tournaments": tournament_list}

@app.get("/upcoming-tournaments")
def upcoming_tournaments():
    response = requests.get(
        "https://api.pandascore.co/csgo/tournaments/upcoming",
        headers=headers
    )
    tournaments = response.json()

    if not tournaments:
        return {"error": "Nenhum campeonato futuro encontrado."}

    tournament_list = []
    for tournament in tournaments[:5]:  # Limita os 5 próximos, opcional
        serie = tournament.get("serie", {})
        tournament_info = {
            "name": serie.get("full_name", tournament.get("name", "Desconhecido")),
            "stage": tournament.get("name", "Desconhecido"),
            "start_date": tournament.get("begin_at", "Data não disponível")
        }
        tournament_list.append(tournament_info)

    return {"tournaments": tournament_list}

@app.get("/game-weapons")
def game_weapons():
    all_weapons = []
    page = 1
    per_page = 100  # máximo suportado pela API da PandaScore

    while True:
        response = requests.get(
            f"https://api.pandascore.co/csgo/weapons?page={page}&per_page={per_page}",
            headers=headers
        )
        weapons = response.json()

        if not weapons:
            break

        for weapon in weapons:
            weapon_info = {
                "name": weapon.get("name", "Desconhecida"),
                "kind": weapon.get("kind", "Desconhecido"),
            }
            all_weapons.append(weapon_info)

        if len(weapons) < per_page:
            break

        page += 1

    if not all_weapons:
        return {"error": "Nenhuma arma encontrada."}

    return {"weapons": all_weapons}