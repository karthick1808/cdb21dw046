import boto3
client = boto3.resource('s3')
for buckets in client.buckets.all():
    if buckets.name.startswith("karthick"):
        print(buckets.name)