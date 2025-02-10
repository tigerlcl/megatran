def solution(input):
    # Split the input string to isolate the phone number part
    parts = input.split()
    phone_number = parts[-1]  # Assuming the last part contains the phone number
    
    # Remove any non-digit characters from the phone number
    digits = ''.join(filter(str.isdigit, phone_number))
    
    # Check if there are enough digits
    if len(digits) < 3:
        return ""  # or handle as needed
    
    # Calculate the middle index
    middle_index = len(digits) // 2
    
    # Extract the middle 3 digits
    if len(digits) % 2 == 0:  # If the length is even
        output = digits[middle_index - 2: middle_index + 1]
    else:  # If the length is odd
        output = digits[middle_index - 1: middle_index + 2]
    
    return output