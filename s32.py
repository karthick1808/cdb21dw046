import boto3
client = boto3.resource('s3')
for buckets in client.buckets.all():
    print(buckets.name)