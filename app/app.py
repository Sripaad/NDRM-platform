from flask import Flask
import logging
import boto3
from botocore.exceptions import ClientError
# fileName = request.args.get('filename')
# bucket_name = request.args.get('bucketName')
app = Flask(__name__)


class ServerSetup(object):
    def __init__(self):

        self.file_name = "file.csv"
        self.bucket_name = "testBucket"
        s3 = boto3.resource('s3', aws_access_key_id="AwsAccessKey", aws_secret_access_key= "AwsSecretAccessKey")

    @app.route("/")
    def index():
      return """
      <h1>Yup the container is running successfully!</h1>
      <p>A sample web-app for running in a container.</p>
      """

    @app.route("/create")
    def create_bucket(self, region=None):
        """Create an S3 bucket in a specified region

        If a region is not specified, the bucket is created in the S3 default
        region (us-east-1).

        :param bucket_name: Bucket to create
        :param region: String region to create bucket in, e.g., 'us-west-2'
        :return: True if bucket created, else False
        """

        # Create bucket
        try:
            if region is None:
                s3_client = boto3.client('s3')
                s3_client.create_bucket(Bucket = self.bucket_name)
            else:
                s3_client = boto3.client('s3', region_name=region)
                location = {'LocationConstraint': region}
                s3_client.create_bucket(Bucket = self.bucket_name,
                                        CreateBucketConfiguration=location)
        except ClientError as e:
            logging.error(e)
            return False
        return True
        # Retrieve the list of existing buckets
        print('Existing buckets:')
        for bucket in response['Buckets']:
            print(f'  {bucket["Name"]}')

    @app.route("/upload")
    def upload_file(self, object_name=None):
        """Upload a file to an S3 bucket

        :param file_name: File to upload
        :param bucket: Bucket to upload to
        :param object_name: S3 object name. If not specified then file_name is used
        :return: True if file was uploaded, else False
        """

        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = self.file_name

        # Upload the file
        s3_client = boto3.client('s3')
        try:
            response = s3_client.upload_file(self.file_name, self.bucket_name, object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True

if __name__ == "__main__":
    serve = ServerSetup()
    app.route('/')(serve.index)
    app.route('/create')(serve.create_bucket)
    app.route('upload')(serve.upload_file)
    app.run(debug=True, host='0.0.0.0')