# flask-backend/app.py

from flask import Flask
from flask_mysqldb import MySQL
from flask_cors import CORS
import os
from config import config_by_name
import routes
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
config_name = os.getenv('FLASK_ENV') or 'development'
app.config.from_object(config_by_name[config_name])

# Initialize MySQL
mysql = MySQL(app)
routes.init_mysql(mysql)

# Enable CORS for all routes
CORS(app)

# Register Blueprints
app.register_blueprint(routes.todos_bp)

if __name__ == '__main__':
    app.run(debug=(config_name == 'development'))
