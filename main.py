from datetime import date
from time import gmtime, strftime

from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def index():
  return jsonify({"message": "Welcome to my Flask App"})


@app.route('/info')
def info():
  return jsonify({
    "current_date": date.today().strftime("%B %d, %Y"),
    "current_time": strftime("%H:%M:%S +0000", gmtime()),
    "status": "OK"
  })


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
