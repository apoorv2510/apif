import os
import json
from flask import Blueprint, jsonify, make_response
from flasgger import swag_from

api_bp = Blueprint("api", __name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(BASE_DIR, "players_large.json")

# Debug print: check path
print(f"🔍 Looking for JSON at: {JSON_FILE}")

# Load players data
players = []

if not os.path.exists(JSON_FILE):
    print(f"⚠️ {JSON_FILE} not found! Creating empty file.")
    with open(JSON_FILE, "w") as f:
        json.dump([], f)
else:
    try:
        with open(JSON_FILE, "r") as f:
            players = json.load(f)
            if not isinstance(players, list):
                raise ValueError("Expected a list of players in JSON file.")
            print(f"✅ Loaded {len(players)} players from JSON.")
    except Exception as e:
        print(f"❌ Error loading players JSON: {e}")
        players = []

# ✅ API: Get All Players
@api_bp.route('/players', methods=['GET'])
@swag_from({
    'responses': {200: {'description': 'Returns a list of players'}},
    'tags': ['Players']
})
def get_players():
    print(f"📤 Returning {len(players)} players")
    response = make_response(jsonify(players))
    response.headers['Content-Type'] = 'application/json'
    return response
