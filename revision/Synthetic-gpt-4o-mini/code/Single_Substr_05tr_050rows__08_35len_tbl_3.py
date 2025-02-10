def solution(input):
    import re
    
    # Find the last occurrence of any special character
    match = re.search(r'[^a-zA-Z0-9](?=[^a-zA-Z0-9]*$)', input)
    
    if match:
        # Extract the substring after the last special character
        if match.start() + 1 < len(input):
            last_substring = input[match.start() + 1:]
        else:
            last_substring = ""
    else:
        # If no special character is found, return an empty string
        return ""
    
    # Limit the length of the output to between 8 and 35 characters
    if 8 <= len(last_substring) <= 35:
        output = last_substring
    elif len(last_substring) < 8:
        output = ""
    else:
        output = last_substring[:35]
    
    return output