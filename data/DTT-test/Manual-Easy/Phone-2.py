def solution(input):
    # Remove any non-numeric characters
    digits = ''.join(filter(str.isdigit, input))
    
    # Format the digits into the desired phone number format
    formatted_number = f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
    
    return formatted_number