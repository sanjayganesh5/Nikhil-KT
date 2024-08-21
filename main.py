import json
import requests


def main(event, context):
    response = requests.get("https://httpbin.org/get")
    json_response = response.json()
    return {
        'statusCode': 200,
        'body': json.dumps(f"Hello from AWS Lambda!\nHTTP Bin Response: {json_response}")
    }
