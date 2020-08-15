import boto3

db = boto3.resource('dynamodb')
table = db.Table("employees")
table.put_item(
    Item = {
        "emp_id" : "2",
        "name" : "Pavi",
        "age" : "21"
    }
)
