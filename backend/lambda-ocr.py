import json

def handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "OCR Extraction Successful",
            "name": "Mahesh Shukla",
            "document_type": "Aadhaar",
            "document_id": "XXXX-XXXX-1234"
        })
    }
