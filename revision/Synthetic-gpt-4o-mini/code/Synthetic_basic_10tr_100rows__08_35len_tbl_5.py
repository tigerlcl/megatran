import re

def solution(input):
    # Convert to lowercase
    input = input.lower()
    
    # Remove special characters (keeping only alphanumeric characters and '&')
    cleaned_input = re.findall(r'[a-z0-9&]', input)
    
    # Rearranging letters and numbers (sorting them)
    output = ''.join(sorted(cleaned_input))
    
    return output