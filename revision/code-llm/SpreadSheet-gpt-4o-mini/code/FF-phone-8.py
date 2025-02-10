def solution(input):
    # Split the input string by spaces and then by hyphen
    parts = input.split()
    phone_number = parts[1].split('-')
    
    # Return the last part of the phone number
    output = phone_number[-1]
    return output