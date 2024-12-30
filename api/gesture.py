import json
import os

def handler(event, context):
    # Read data from the frontend (gesture data)
    body = json.loads(event['body'])
    fingers_up = body.get('fingersUp', [])
    
    # Perform processing (for example, execute virtual mouse commands, etc.)
    print(f"Fingers up: {fingers_up}")
    
    # Return response to the frontend
    return {
        "statusCode": 200,
        "body": json.dumps({"status": "success", "fingers_up": fingers_up})
    }
