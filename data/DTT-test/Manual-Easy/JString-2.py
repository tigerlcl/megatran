import json

def solution(input):
    # Parse the JSON input
    data = json.loads(input)
    # Extract the business_id
    business_id = data.get("business_id")
    return business_id