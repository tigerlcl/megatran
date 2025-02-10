def solution(input):
    # Split the input string by spaces to isolate the phone number part
    parts = input.split()
    # The phone number is the second part, split by '-'
    phone_number = parts[1]
    # Split the phone number by '-' and take the second part
    output = phone_number.split('-')[1]
    return output