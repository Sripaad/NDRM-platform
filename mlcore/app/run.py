import pythonUtils.pushData
import os
import json
from flask import Flask
from flask import jsonify

app = Flask(__name__)

pd = pythonUtils.pushData.Server()
snsTopicArn = 'arn:aws:sns:us-east-1:000000000000:scrapperNotif'
snsEndPoint = 'http://mlcore-container:6543/getM'
snsResponse = pd.subscribe_topic(snsTopicArn, snsEndPoint)
snsSubscribeArn = "arn:aws:sns:us-east-1:000000000000:scrapperNotif:72d3b99c-8c20-419e-9fb3-474c778d2c23"

@app.route('/')
def index():
    return "<h1>Hello from Mlcore contaniner<h1><br>"

def getFileNames():
    sqsResponseMessage = pd.receive_message()
    fileNames = []
    for i in range(0,len(sqsResponseMessage["Messages"])):
        fileNames.append(sqsResponseMessage["Messages"][i]["Body"])
    return jsonify(fileNames)


if __name__ == '__main__':
    app.run(debug=True,port=6543, host='0.0.0.0')