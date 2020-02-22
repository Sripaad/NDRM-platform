#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

class Server():

    def create_buckets(region=None):
        os.system('aws --endpoint-url=http://localstack-container:4572 s3 mb s3://unstructured-db')
        os.system('aws --endpoint-url=http://localstack-container:4572 s3 mb s3://globe-db')
        os.system('aws --endpoint-url=http://localstack-container:4572 s3 mb s3://structured-db')
        print("buckets created")
        return True

    def upload_files(self,fileName,bucketName):
        # Upload the file
        os.system('aws --endpoint-url=http://localstack-container:4572 s3 cp ' + fileName + ' s3://' + bucketName +'/')
        return True
    
    def create_queue(self):
        os.system('aws --endpoint-url=http://localstack-container:4576 sqs create-queue --queue-name scrapperQ')
        return True

    def send_message(self, messageBody):
        os.system('aws --endpoint-url=http://localstack-container:4576 sqs send-message --queue-url http://localstack-container:4576/queue/scrapperQ --message-body ' + messageBody)
        return True
    
    def receive_message(self):
        os.system('aws --endpoint-url=http://localstack-container:4576 sqs receive-message --queue-url http://localstack-container:4576/queue/scrapperQ')
    
    def create_notification(self,topicName):
        os.system('aws --endpoint-url http://localstack-container:4575 sns create-topic --name ' + topicName)
        return True

    def publish_topic(self, topicArn, message):
        os.system('aws --endpoint-url=http://localstack-container:4575 sns publish  --topic-arn ' + topicArn + ' --message ' + message)
    
    def subscribe_topic(self, topicArn, endPoint):
        os.system('aws --endpoint-url=http://localstack-container:4575 sns subscribe --topic-arn ' + topicArn + ' --protocol http --notification-endpoint ' + endPoint)
    
    def awsConfigure(self):
        os.system('export AWS_SECRET_ACCESS_KEY=AwsSecretAccessKey')
        os.system('export AWS_ACCESS_KEY_ID=AwsAccessKey')
        os.system('export AWS_DEFAULT_REGION=us-east-1')
        S = Server()
        if S.create_buckets():
            if S.create_notification('scrapperNotif'):
                print("Bucket created and file uploaded")
                print("Topic Created")
