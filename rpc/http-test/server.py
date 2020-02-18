from flask import Flask
from flask import request, jsonify


app = Flask(__name__)

@app.route('/spin', methods=['POST'])
def spin():
    data = request.json
    print(data)
    if not data:
        return jsonify(dict(data='', code=400))
    u_id = data.get('u_id')
    return jsonify(dict(data=u_id, code=200))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8081')
    