import re

def solution(input):
    # Use regex to find all sequences of digits
    parts = re.findall(r'\d+', input)
    
    # Join the parts with a dot
    output = '.'.join(parts)
    
    return output