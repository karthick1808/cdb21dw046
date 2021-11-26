import boto3
client = boto3.client('s3')
response = client.create_bucket(Bucket='karthick-boto3-example-bucket',CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})
print(response)

CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }