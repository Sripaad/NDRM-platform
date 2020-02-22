import twint
import os 
import sys
import pushData


def Scrapp(keyWord):
    pd = pushData.Server()
    command = 'twint -s ' + keyWord + ' -o ' + keyWord + '.csv'
    op = os.system(command)
    if op == 0:
        fileName = keyWord + '.csv'
        bucketName = 'unstructured-db'
        print(fileName, bucketName, command)
        if pd.upload_files(fileName,bucketName):
            pd.send_message(fileName)        
            topicArn = 'arn:aws:sns:us-east-1:000000000000:scrapperNotif'
            pd.publish_topic(topicArn, fileName)
            print("messagePublished to SNS and SQS")
        
