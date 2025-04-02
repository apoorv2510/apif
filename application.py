from flask import Flask
from flasgger import Swagger
from flask_cors import CORS  # ✅ Import CORS
import apiap  # ✅ Direct import without `sports_api.` prefix

application = Flask(__name__)  # ✅ AWS Beanstalk requires "application"
CORS(application, resources={r"/*": {"origins": "*"}})  # ✅ Enable CORS for all routes

# ✅ Configure Swagger with OpenAPI specification URL
swagger = Swagger(application, template={
    "swagger": "2.0",
    "info": {
        "title": "Sports Players API",
        "description": "API for retrieving football players and their details.",
        "version": "1.0.0",
        "contact": {
            "name": "Developer Support",
            "email": "support@example.com"
        }
    },
    "host": "playersapi.us-east-1.elasticbeanstalk.com",  # ✅ Update with your Elastic Beanstalk URL
    "schemes": ["http"],
    "basePath": "/api",
    "paths": {
        "/players": {
            "get": {
                "summary": "Get all players",
                "description": "Returns a list of football players.",
                "responses": {
                    "200": {
                        "description": "A JSON array of players",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/definitions/Player"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    },
    "definitions": {
        "Player": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "team": {"type": "string"},
                "position": {"type": "string"},
                "nationality": {"type": "string"},
                "age": {"type": "integer"}
            }
        }
    }
})

# ✅ Register API Blueprint
application.register_blueprint(apiap.api_bp, url_prefix="/api")  # ✅ Direct reference

@application.route('/')
def home():
    return "<h1>Sports API is Running 🚀</h1><p>Use <b>/api/players</b> to access player data.</p>"

if __name__ == '__main__':
    application.run(debug=True, host="0.0.0.0", port=8080)
