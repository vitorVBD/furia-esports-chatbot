from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Libera acesso do React (frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # porta padrão do Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = "VyuJGyw9ejTo66QJLPuD5eRsXVTiR3302URgCmKNzwpnMZN3j48"
headers = {"Authorization": f"Bearer {API_KEY}"}


@app.get("/next-match")
def next_match():
    team_search = requests.get("https://api.pandascore.co/csgo/teams", headers=headers, params={"search[name]": "FURIA"}).json()
    if not team_search:
        return {"error": "FURIA não encontrada"}
    furia_id = team_search[0]["id"]

    matches = requests.get("https://api.pandascore.co/csgo/matches/upcoming", headers=headers).json()
    furia_matches = [m for m in matches if any(o["opponent"]["id"] == furia_id for o in m["opponents"])]

    if furia_matches:
        match = furia_matches[0]
        return {
            "name": match["name"],
            "date": match["begin_at"],
            "opponents": [op["opponent"]["name"] for op in match["opponents"]]
        }
    else:
        return {"message": "Nenhuma partida futura encontrada."}

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

@app.get("/last-match")
def last_match(gender: str = "masculino"):
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

    response = requests.get(
        f"https://api.pandascore.co/csgo/matches/past?filter[team]={team['id']}",
        headers=headers
    )
    matches = response.json().get("data", [])

    if not matches:
        return {"message": f"Nenhum resultado encontrado para o time {team['name']}."}

    filtered_matches = [
    match for match in matches
    if isinstance(match, dict) and match.get("opponents") and
       any(isinstance(op, dict) and op.get("opponent", {}).get("name") == team["name"] for op in match["opponents"])
]

    if not filtered_matches:
        return {"message": f"Nenhum resultado encontrado para o time {team['name']}."}

    match = filtered_matches[0]

    return {
        "match_name": match["name"],
        "result": f"{match['opponents'][0]['opponent']['name']} {match['results'][0]['score']} x {match['results'][1]['score']} {match['opponents'][1]['opponent']['name']}",
        "date": match["begin_at"]
    }

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