from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'

db = SQLAlchemy(app)

# Dummy data for demonstration purposes
items = [{'id': 1, 'name': 'Item 1'}, {'id': 2, 'name': 'Item 2'}]
categories = [{'id': 1, 'name': 'Category 1'}, {'id': 2, 'name': 'Category 2'}]
users = [{'id': 1, 'username': 'user1', 'email': 'user1@example.com'}, {'id': 2, 'username': 'user2', 'email': 'user2@example.com'}]

@app.route('/')
def hello_world():
    return 'Hello, World!'
# Routes for items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({'message': 'Item not found'}), 404

# Routes for categories
@app.route('/categories', methods=['GET'])
def get_categories():
    return jsonify(categories)

@app.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    category = next((category for category in categories if category['id'] == category_id), None)
    if category:
        return jsonify(category)
    return jsonify({'message': 'Category not found'}), 404

# Routes for users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({'message': 'User not found'}), 404

# Routes for authentication (dummy implementation)
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    # Dummy authentication logic
    if username == 'example_user' and password == 'example_password':
        return jsonify({'message': 'Login successful'})
    return jsonify({'message': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(debug=True)
