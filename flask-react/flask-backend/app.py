# project/app.py

from flask import Flask
from flask_mysqldb import MySQL
from flask_cors import CORS
from config import Config
import routes

app = Flask(__name__)
app.config.from_object(Config)

# Initialize MySQL
mysql = MySQL(app)
routes.init_mysql(mysql)

# Enable CORS for all routes
CORS(app)

# Register Blueprints
app.register_blueprint(routes.todos_bp)

if __name__ == '__main__':
    app.run(debug=True)
