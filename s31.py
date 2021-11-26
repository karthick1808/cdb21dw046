import boto3
client = boto3.client('s3')
response = client.list_objects_v2(Bucket='karthick1808-cdb21dw043')
print(response)