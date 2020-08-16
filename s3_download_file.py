import boto3

s3 = boto3.client('s3')
s3.download_file('multipart-aakash', 'sample.txt', 'file2.txt')
list = s3.list_buckets()
print(list)
