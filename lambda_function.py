import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('vaccine-registration')

def lambda_handler(event, context):
    print("Received event:", event)
    
    try:
        name = event['name']
        fishId = event['fishId']
        vaccDt = event['vaccineDate']
    except KeyError as e:
        return {
            'statusCode': 400,
            'body': json.dumps(f'Missing parameter: {e}')
        }

    now = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    # Store in DynamoDB
    response = table.put_item(
        Item={
            'id': fishId,
            'name': name,
            'vacDate': vaccDt,
            'registTime': now
        }
    )

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type, Authorization'
        },
        'body': json.dumps('Registration succeeded for, ' + name)
    }
