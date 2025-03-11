import os
from flask import Flask, jsonify
import requests

app = Flask(__name__)

AUX_SERVICE_HOST = os.environ.get('AUX_SERVICE_HOST', 'http://127.0.0.1:4000')  # Default for local

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        aux_response = requests.get(f'{AUX_SERVICE_HOST}/aux_data')
        aux_data = aux_response.json()
        data = {'message': 'Hello from the Main API!', 'aux_data': aux_data}
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)