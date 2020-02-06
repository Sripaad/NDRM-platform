from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
    listl = []
    listl = os.listdir("../files")
    return jsonify(listl)

if __name__ == '__main__':
    app.run(debug=True,port=6543, host='0.0.0.0')