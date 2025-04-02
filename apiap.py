import os
import json
from flask import Blueprint, jsonify, request
from flasgger import swag_from

# ✅ Create Blueprint
api_bp = Blueprint("api", __name__)

# ✅ File path for dataset (absolute path to ensure consistency)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_FILE = os.path.join(BASE_DIR, "players_large.json")

# ✅ Ensure JSON file exists
if not os.path.exists(JSON_FILE):
    print(f"⚠️ {JSON_FILE} not found. Creating a new file...")
    with open(JSON_FILE, "w") as file:
        json.dump([], file)  # Initialize empty JSON

# ✅ Load dataset
with open(JSON_FILE, "r") as file:
    try:
        players = json.load(file)
        if not isinstance(players, list):
            raise ValueError("Invalid JSON format. Expected a list.")
    except json.JSONDecodeError:
        print("❌ Error: JSON file is corrupted. Resetting dataset...")
        players = []
        with open(JSON_FILE, "w") as file:
            json.dump(players, file, indent=4)

# ✅ API: Get All Players
@api_bp.route('/players', methods=['GET'])
@swag_from({
    'responses': {200: {'description': 'Returns a list of players'}},
    'tags': ['Players']
})
def get_players():
    return jsonify(players)
