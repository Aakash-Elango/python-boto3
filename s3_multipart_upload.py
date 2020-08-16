import boto3
from boto3.s3.transfer import TransferConfig

GB = 1024 ** 3
config = TransferConfig(multipart_threshold=5*GB)

s3 = boto3.client('s3')
s3.upload_file('/home/aakash/Videos/DontBreatheHD.mp4', 'multipart-aakash', 'DontBreatheHD.mp4', Config=config)
list = s3.list_buckets()
print(list)
