from flask import Flask
from flasgger import Swagger
import apiap  # ✅ Direct import without `application.` prefix

application = Flask(__name__)  # ✅ AWS Beanstalk requires "application"
Swagger(application)

# ✅ Register API Blueprint
application.register_blueprint(apiap.api_bp, url_prefix="/api")  # ✅ Direct reference

@application.route('/')
def home():
    return "<h1>Sports API is Running 🚀</h1><p>Use <b>/api/players</b> to access player data.</p>"

if __name__ == '__main__':
    application.run(debug=True, host="0.0.0.0", port=5000)
