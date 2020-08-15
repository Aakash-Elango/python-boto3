import boto3

db = boto3.resource('dynamodb')
table = db.Table("employees")
data = table.get_item(
    Key = {
        "emp_id" : "1"
    }
)
print (data["Item"])
