from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username == 'admin' and password == 'password123':
        app.logger.info(f"SUCCESSFUL LOGIN: {username}")
        return jsonify({"message": "Login successful"}), 200
    else:
        app.logger.warning(f"FAILED LOGIN ATTEMPT: {username}")
        return jsonify({"message": "Login failed"}), 401

@app.route('/')
def home():
    return "Flask login app running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
