import json

def solution(input):
    data = json.loads(input)
    return data.get("department")