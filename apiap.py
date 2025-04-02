from flask import Blueprint, jsonify
from flasgger import swag_from

# ✅ Create Blueprint
api_bp = Blueprint("api", __name__)

# ✅ Embedded Player Data (no file reading)
players = [
    {"id": 1, "name": "Lionel Messi", "team": "Inter Miami", "nationality": "Argentina", "position": "Forward", "age": 36},
    {"id": 2, "name": "Cristiano Ronaldo", "team": "Al-Nassr", "nationality": "Portugal", "position": "Forward", "age": 39},
    {"id": 3, "name": "Neymar Jr", "team": "Al-Hilal", "nationality": "Brazil", "position": "Forward", "age": 32},
    {"id": 4, "name": "Kylian Mbappe", "team": "Paris Saint-Germain", "nationality": "France", "position": "Forward", "age": 25},
    {"id": 5, "name": "Erling Haaland", "team": "Manchester City", "nationality": "Norway", "position": "Forward", "age": 23},
    {"id": 6, "name": "Kevin De Bruyne", "team": "Manchester City", "nationality": "Belgium", "position": "Midfielder", "age": 33},
    {"id": 7, "name": "Luka Modric", "team": "Real Madrid", "nationality": "Croatia", "position": "Midfielder", "age": 38},
    {"id": 8, "name": "Virgil van Dijk", "team": "Liverpool", "nationality": "Netherlands", "position": "Defender", "age": 32},
    {"id": 9, "name": "Mohamed Salah", "team": "Liverpool", "nationality": "Egypt", "position": "Forward", "age": 31},
    {"id": 10, "name": "Robert Lewandowski", "team": "Barcelona", "nationality": "Poland", "position": "Forward", "age": 35},
    {"id": 11, "name": "Harry Kane", "team": "Bayern Munich", "nationality": "England", "position": "Forward", "age": 30},
    {"id": 12, "name": "Bruno Fernandes", "team": "Manchester United", "nationality": "Portugal", "position": "Midfielder", "age": 29},
    {"id": 13, "name": "Marcus Rashford", "team": "Manchester United", "nationality": "England", "position": "Forward", "age": 26},
    {"id": 14, "name": "Antoine Griezmann", "team": "Atletico Madrid", "nationality": "France", "position": "Forward", "age": 32},
    {"id": 15, "name": "Jude Bellingham", "team": "Real Madrid", "nationality": "England", "position": "Midfielder", "age": 20},
    {"id": 16, "name": "Vinicius Jr", "team": "Real Madrid", "nationality": "Brazil", "position": "Forward", "age": 23},
    {"id": 17, "name": "Rodri", "team": "Manchester City", "nationality": "Spain", "position": "Midfielder", "age": 27},
    {"id": 18, "name": "Pedri", "team": "Barcelona", "nationality": "Spain", "position": "Midfielder", "age": 21},
    {"id": 19, "name": "Joao Cancelo", "team": "Barcelona", "nationality": "Portugal", "position": "Defender", "age": 29},
    {"id": 20, "name": "Gavi", "team": "Barcelona", "nationality": "Spain", "position": "Midfielder", "age": 19},
    {"id": 21, "name": "Alisson Becker", "team": "Liverpool", "nationality": "Brazil", "position": "Goalkeeper", "age": 31},
    {"id": 22, "name": "Marc-Andre ter Stegen", "team": "Barcelona", "nationality": "Germany", "position": "Goalkeeper", "age": 31},
    {"id": 23, "name": "Thibaut Courtois", "team": "Real Madrid", "nationality": "Belgium", "position": "Goalkeeper", "age": 32},
    {"id": 24, "name": "Rafael Leao", "team": "AC Milan", "nationality": "Portugal", "position": "Forward", "age": 24},
    {"id": 25, "name": "Bernardo Silva", "team": "Manchester City", "nationality": "Portugal", "position": "Midfielder", "age": 29},
    {"id": 26, "name": "Joshua Kimmich", "team": "Bayern Munich", "nationality": "Germany", "position": "Midfielder", "age": 29},
    {"id": 27, "name": "Federico Valverde", "team": "Real Madrid", "nationality": "Uruguay", "position": "Midfielder", "age": 25},
    {"id": 28, "name": "Sadio Mane", "team": "Al-Nassr", "nationality": "Senegal", "position": "Forward", "age": 32},
    {"id": 29, "name": "Serge Gnabry", "team": "Bayern Munich", "nationality": "Germany", "position": "Forward", "age": 28},
    {"id": 30, "name": "Son Heung-min", "team": "Tottenham Hotspur", "nationality": "South Korea", "position": "Forward", "age": 31},
    {"id": 31, "name": "Apoorv", "team": "Tottenham Hotspur", "nationality": "South Korea", "position": "Forward", "age": 31},
    {"id": 32, "name": "Anuj", "team": "Barcelona", "nationality": "India", "position": "Forward", "age": 20}
]

# ✅ API: Get All Players
@api_bp.route('/players', methods=['GET'])
@swag_from({
    'responses': {200: {'description': 'Returns a list of players'}},
    'tags': ['Players']
})
def get_players():
    return jsonify(players)
