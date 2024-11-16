from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello_world():
    return jsonify({'message': 'Hello, World!'})

@app.route('/api/goodbye', methods=['GET'])
def goodbye():
    return jsonify({'message': 'Goodbye!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
