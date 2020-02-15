import pushData
import os
import json
from flask import Flask
from flask import jsonify

app = Flask(__name__)

pd = pushData.Server()
snsTopicArn = 'arn:aws:sns:us-east-1:000000000000:scrapperNotif'
snsEndPoint = 'http://mlcore-container:6543/getM'
snsResponse = pd.subscribe_topic(snsTopicArn, snsEndPoint)
snsSubscribeArn = "arn:aws:sns:us-east-1:000000000000:scrapperNotif:72d3b99c-8c20-419e-9fb3-474c778d2c23"

@app.route('/')
def index():
    return "<h1>Hello this is the Mlcore contaniner<h1><br>"


@app.route('/getM')
def getM():
    sqsResponse = pd.receive_message()
    jsonMessage = json.dumps(sqsResponse)  
    for i in range()
    jsonMessageBody = json.dumps(sqsResponse["Messages"][0]["Body"])
    jsonMessageBodies = []
    jsonMessageBodies = jsonMessageBodies.append[jsonMessageBody]


if __name__ == '__main__':
    app.run(debug=True,port=6543, host='0.0.0.0')