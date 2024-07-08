import re

def solution(input):
    # Use regex to remove HTML tags
    output = re.sub(r'<.*?>', '', input)
    return output