import boto3

ec2 = boto3.client('ec2')
ec2.start_instances(InstanceIds=['INSTANCE_ID'])
response = ec2.describe_instances()
print(response)
