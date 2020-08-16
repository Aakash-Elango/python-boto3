import boto3

s3 = boto3.client('s3')
s3.upload_file('file.txt', 'Demo-aakash', 'sample.txt')
list = s3.list_buckets()
print(list)
