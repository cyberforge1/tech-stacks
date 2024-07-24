# project/routes.py

from flask import Blueprint, jsonify, request
from flask_mysqldb import MySQL
import MySQLdb.cursors

todos_bp = Blueprint('todos', __name__)

mysql = None

def init_mysql(app_mysql):
    global mysql
    mysql = app_mysql

@todos_bp.route('/helloworld')
def hello_world():
    return "Hello World"

@todos_bp.route('/')
def home():
    return jsonify(message="Home Page")

@todos_bp.route('/todo/', methods=['POST'])
def add_todo():
    data = request.json
    title = data['title']
    
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO todos (title) VALUES (%s)', (title,))
    mysql.connection.commit()
    cursor.close()
    
    return jsonify(message="Todo added successfully"), 201

@todos_bp.route('/todo/', methods=['GET'])
def get_todos():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM todos')
    todos = cursor.fetchall()
    cursor.close()
    
    return jsonify(todos)

@todos_bp.route('/todo/<int:id>', methods=['PUT'])
def update_todo(id):
    data = request.json
    title = data['title']
    
    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE todos SET title = %s WHERE id = %s', (title, id))
    mysql.connection.commit()
    cursor.close()
    
    return jsonify(message="Todo updated successfully")

@todos_bp.route('/todo/<int:id>', methods=['DELETE'])
def delete_todo(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM todos WHERE id = %s', (id,))
    mysql.connection.commit()
    cursor.close()
    
    return jsonify(message="Todo deleted successfully")
