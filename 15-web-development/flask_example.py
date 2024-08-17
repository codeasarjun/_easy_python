# flask_example.py

from flask import Flask, jsonify, request

app = Flask(__name__)

# a route for the root URL
@app.route('/')
def home():
    return "Welcome to the Flask Example!"

#  a route for a JSON response
@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')
    return jsonify({'message': f'Hello, {name}!'})

if __name__ == '__main__':
    app.run(debug=True)
