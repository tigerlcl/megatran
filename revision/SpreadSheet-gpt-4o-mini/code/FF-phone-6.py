def solution(input):
    # Remove any non-digit characters from the input
    digits = ''.join(filter(str.isdigit, input))
    
    # Check if there are at least 3 digits
    if len(digits) < 3:
        return ''  # or raise an error based on requirements
    
    # Calculate the middle index
    middle_index = len(digits) // 2
    
    # Extract the middle 3 digits
    if len(digits) % 2 == 0:  # Even length
        output = digits[middle_index - 1:middle_index + 2]
    else:  # Odd length
        output = digits[middle_index - 1:middle_index + 2]
    
    return output