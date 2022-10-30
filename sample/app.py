import json

def lambda_handler(event, context):
    rc = event['requestContext']
    identityId = rc['authorizer']['iam']['cognitoIdentity']['identityId']
    method = rc['http']['method']
    path = rc['http']['path']
    print(f'method:{method} path:{path} identityId:{identityId}')

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
