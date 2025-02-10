def solution(input):
    # Find the position of the last special character
    special_chars = set("!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~")
    last_special_index = -1
    
    for i, char in enumerate(input):
        if char in special_chars:
            last_special_index = i
    
    # If no special character is found, return the input as is
    if last_special_index == -1:
        return input
    
    # Return the substring up to and including the last special character
    output = input[:last_special_index + 1]
    return output