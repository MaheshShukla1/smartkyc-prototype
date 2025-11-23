import json

def handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "risk_score": "LOW",
            "recommendation": "AUTO-APPROVE"
        })
    }
