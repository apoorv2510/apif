import os
import json
from flask import Blueprint, jsonify
from flasgger import swag_from

api_bp = Blueprint("api", __name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(BASE_DIR, "players_large.json")

# Debug print: check path
print(f"🔍 Looking for JSON at: {JSON_FILE}")

# Ensure JSON exists
if not os.path.exists(JSON_FILE):
    print(f"⚠️ {JSON_FILE} not found! Creating empty file.")
    with open(JSON_FILE, "w") as f:
        json.dump([], f)
    players = []
else:
    with open(JSON_FILE, "r") as f:
        try:
            players = json.load(f)
            if not isinstance(players, list):
                raise ValueError("Expected list in JSON")
            print(f"✅ Loaded {len(players)} players")
        except Exception as e:
            print(f"❌ Failed to load players: {e}")
            players = []

@api_bp.route('/api/players', methods=['GET'])
@swag_from({
    'responses': {200: {'description': 'Returns a list of players'}},
    'tags': ['Players']
})
def get_players():
    return jsonify(players)
