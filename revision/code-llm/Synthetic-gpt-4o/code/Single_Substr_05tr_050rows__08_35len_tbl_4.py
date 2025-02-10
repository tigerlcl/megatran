def solution(input):
    # Find the first occurrence of a digit in the input string
    first_digit_index = next((i for i, c in enumerate(input) if c.isdigit()), None)
    
    # If no digit is found, return an empty string
    if first_digit_index is None:
        return ""
    
    # Extract the substring starting from the first digit
    output = input[first_digit_index:]
    
    # Find the first occurrence of an uppercase letter in the extracted substring
    first_uppercase_index = next((i for i, c in enumerate(output) if c.isupper()), None)
    
    # If no uppercase letter is found, return the entire extracted substring
    if first_uppercase_index is None:
        return output
    
    # Extract the substring starting from the first uppercase letter
    output = output[first_uppercase_index:]
    
    return output