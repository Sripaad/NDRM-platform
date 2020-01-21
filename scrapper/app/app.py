#!/usr/bin/python
import logging
import boto3
from botocore.exceptions import ClientError
import os
from flask import Flask
from flask_classful import FlaskView


# app = Flask(__name__)

class Server():
    def __init__(self):

        self.file_name = "file.csv"         # fileName = request.args.get('filename')
        self.bucket_name = "testBucket"     # bucket_name = request.args.get('bucketName')
        self.s3 = boto3.resource('s3',
                            endpoint_url = "http://localstack-container:4572", 
                            aws_access_key_id = "AwsAccessKey",
                            aws_secret_access_key = "AwsSecretAccessKey")
        self.region_name = None
        self.object_name = "scrapped-script"
        
    # @app.route("/")
    # def index():
    #   return """
    #   <h1>Yup the service is running successfully!</h1>
    #   <p>A sample web-app for running in a container.</p>
    #   """
    # @app.route("/scrap")
    def scrap():
        os.system('twint -u _hohosanta -o file.csv') # request.args.get('twint cli command')
        print("scrapped successfully")
        return 0
    #     return """<h1>Scrapped successfully!</h1>"""
        
    # @app.route("/create")
    def create_bucket(region = None):
        """Create an S3 bucket in a specified region

        If a region is not specified, the bucket is created in the S3 default
        region (us-east-1).

        :param bucket_name: Bucket to create
        :param region: String region to create bucket in, e.g., 'us-west-2'
        :return: True if bucket created, else False
        """
        # Create bucket
        s3 = boto3.resource('s3',
                            endpoint_url = "http://localstack-container:4572", 
                            aws_access_key_id = "AwsAccessKey",
                            aws_secret_access_key = "AwsSecretAccessKey")
        bucket_name = "testBucket"
        try:
            if region is None:
                s3_client = boto3.client('s3')
                s3_client = boto3.resource('s3',
                            endpoint_url = "http://localstack-container:4572", 
                            aws_access_key_id = "AwsAccessKey",
                            aws_secret_access_key = "AwsSecretAccessKey")
                s3_client.create_bucket(Bucket = bucket_name)
            # else:
            #     print(region)
            #     s3_client = boto3.client('s3', region_name=region)
            #     location = {'LocationConstraint': region}
            #     s3_client.create_bucket(Bucket = self.bucket_name,
            #                             CreateBucketConfiguration=location)
        except ClientError as e:
            logging.error(e)
            return False
        return True
        # return """<h1>Created Bucket successfully!</h1>"""
    
    # @app.route("/upload")
    def upload_file(object_name = None):
        """Upload a file to an S3 bucket

        :param file_name: File to upload
        :param bucket: Bucket to upload to
        :param object_name: S3 object name. If not specified then file_name is used
        :return: True if file was uploaded, else False
        """
        s3_client = boto3.client('s3')
        s3_client = boto3.resource('s3',
                            endpoint_url = "http://localstack-container:4572", 
                            aws_access_key_id = "AwsAccessKey",
                            aws_secret_access_key = "AwsSecretAccessKey")
        # Listing the buckets
        response = os.system('aws --endpoint-url=http://localstack-container:4572 s3 ls')
        print(response)
        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = file_name

        # Upload the file
        try:
            response = s3_client.upload_file(file_name, bucket_name, object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True
        # return """<h1>Uploaded successfully!</h1>"""
    def create_queue():
        os.system('aws --endpoint http://localstack-container:4576 sqs create-queue --queue-name scrapQ')

S = Server()
if S.create_bucket() == True:
    if S.scrap == 0:
        S.upload_file()
        S.create_queue()
        print("Bucket created and file uploaded")
        print("Queues Created")

# if __name__ == "__main__":
#     serve = Server()
#     app.route('/')(serve.index)
#     app.route('/scrap')(serve.scrap)
#     app.route('/create')(serve.create_bucket)
#     app.route('upload')(serve.upload_file)
#     app.run(debug=True, host='0.0.0.0')