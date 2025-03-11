from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/aux_data', methods=['GET'])
def aux_data():
    return jsonify({'message': 'Data from auxiliary service'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)