import boto3
client = boto3.client('s3')
response = client.delete_objects(Bucket='karthick1808-cdb21dw043',Delete={'Objects': [{'Key': 'war.txt','VersionId': 'null'},],'Quiet': True})
print(response)