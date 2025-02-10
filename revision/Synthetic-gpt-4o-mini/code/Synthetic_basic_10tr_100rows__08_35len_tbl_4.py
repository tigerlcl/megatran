import re

def solution(input):
    # Convert to lowercase
    output = input.lower()
    # Replace special characters with underscores, but keep periods
    output = re.sub(r'[^a-z0-9.]', '_', output)
    # Truncate to 64 characters
    output = output[:64]
    return output