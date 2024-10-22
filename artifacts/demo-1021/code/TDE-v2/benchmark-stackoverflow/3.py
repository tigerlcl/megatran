import re

def solution(input):
    # Remove HTML tags using regex
    output = re.sub(r'<[^>]+>', ' ', input)
    # Replace multiple spaces with a single space and strip leading/trailing spaces
    output = re.sub(r'\s+', ' ', output).strip()
    return output