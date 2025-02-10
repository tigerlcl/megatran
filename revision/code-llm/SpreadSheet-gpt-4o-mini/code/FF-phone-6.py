def solution(input):
    # Split the input string by spaces to isolate the phone number part
    parts = input.split()
    
    # The phone number is the second part of the split input
    phone_number = parts[1]
    
    # Split the phone number by the hyphen to get the desired segment
    segments = phone_number.split('-')
    
    # The desired output is the first segment of the phone number
    output = segments[0]
    
    return output