import boto3
client = boto3.client('s3')
response = client.delete_object(Bucket='karthick1808-cdb21dw043',Key='war.txt',)
print(response)