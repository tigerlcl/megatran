def solution(input):
    # Find the position of the first digit
    first_digit_index = next((i for i, char in enumerate(input) if char.isdigit()), None)
    
    # If no digit is found, return an empty string
    if first_digit_index is None:
        return ""
    
    # Find the position of the last alphabetic character before the first digit
    last_alpha_index = next((i for i in range(first_digit_index - 1, -1, -1) if input[i].isalpha()), None)
    
    # If no alphabetic character is found before the first digit, return an empty string
    if last_alpha_index is None:
        return ""
    
    # Extract the substring from the last alphabetic character to the end of the input
    output = input[last_alpha_index + 1:]
    
    return output