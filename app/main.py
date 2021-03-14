from flask import Flask, Response
import requests


app = Flask(__name__)


@app.route('/')
def hello():
    return Response(requests.get('http://192.168.5.152/api/air/state').content, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80)
 