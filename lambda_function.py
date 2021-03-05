import json
import urllib3
import main

def lambda_handler(event, context):
    http = urllib3.PoolManager()
    
    data = {"text": "Sample Message From Lambda Function"}
    
    r = http.request("POST",
                    "https://hooks.slack.com/services/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",
                    body = json.dumps(data),
                    headers = {"Content-Type": "application/json"})
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
