import json

def handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "face_match_score": 98.7,
            "liveness_detected": True
        })
    }
