from flask import Flask
from flask import request, jsonify
import time


app = Flask(__name__)

@app.route('/spin', methods=['POST'])
def spin():
    time.sleep(1)
    data = request.json
    if not data:
        return jsonify(dict(data='', code=400))
    u_id = data.get('u_id')
    return jsonify(dict(data=u_id, code=200))

# gunicorn -b localhost:8081 -k gevent server:app -w 2
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8081')
    