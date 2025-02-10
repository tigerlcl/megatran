def solution(input):
    # Find the first occurrence of a digit in the input string
    first_digit_index = next((i for i, c in enumerate(input) if c.isdigit()), None)
    
    # If no digit is found, return an empty string
    if first_digit_index is None:
        return ""
    
    # Extract the substring starting from the first digit
    output = input[first_digit_index:]
    
    # Find the first occurrence of a non-digit character after the first digit
    first_non_digit_index = next((i for i, c in enumerate(output) if not c.isdigit()), None)
    
    # If no non-digit character is found, return the entire substring
    if first_non_digit_index is None:
        return output
    
    # Extract the substring starting from the first non-digit character
    output = output[first_non_digit_index:]
    
    # Find the last occurrence of a digit in the output string
    last_digit_index = max((i for i, c in enumerate(output) if c.isdigit()), default=None)
    
    # If no digit is found, return the entire substring
    if last_digit_index is None:
        return output
    
    # Extract the substring up to and including the last digit
    output = output[:last_digit_index + 1]
    
    return output