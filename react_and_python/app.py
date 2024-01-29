from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample data
items = [{'id': 1, 'name': 'Item 1'}, {'id': 2, 'name': 'Item 2'}]

@app.route('/api/items', methods=['GET'])
def get_items():
    return jsonify(items)

if __name__ == '__main__':
    app.run(debug=True)
