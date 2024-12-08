from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    """Serve the index.html file."""
    return send_from_directory(os.getcwd(), 'index.html')

@app.route('/add', methods=['POST'])
def add_route():
    data = request.json
    result = float(data['x']) + float(data['y'])
    return jsonify({'result': result})

@app.route('/subtract', methods=['POST'])
def subtract_route():
    data = request.json
    result = float(data['x']) - float(data['y'])
    return jsonify({'result': result})

@app.route('/multiply', methods=['POST'])
def multiply_route():
    data = request.json
    result = float(data['x']) * float(data['y'])
    return jsonify({'result': result})

@app.route('/divide', methods=['POST'])
def divide_route():
    data = request.json
    if data['y'] == 0:
        return jsonify({'error': "Division by zero is undefined."}), 400
    result = float(data['x']) / float(data['y'])
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)