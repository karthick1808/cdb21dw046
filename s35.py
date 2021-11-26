import boto3
client = boto3.client('s3')
response = client.delete_bucket(Bucket='demo-my-bucket-0407')
print(response)