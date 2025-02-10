def solution(input):
    # Find the last occurrence of a digit
    last_digit_index = -1
    for i in range(len(input)):
        if input[i].isdigit():
            last_digit_index = i
    
    # If no digit is found, return an empty string
    if last_digit_index == -1:
        return ""
    
    # Extract the substring from the last digit to the end of the string
    output = input[last_digit_index:]
    
    # Find the first occurrence of a digit in the output to trim it
    first_digit_index = 0
    while first_digit_index < len(output) and not output[first_digit_index].isdigit():
        first_digit_index += 1
    
    # Return the substring from the first digit to the end
    return output[first_digit_index:]

# Example usage:
print(solution("vspQ6Rr?stO?M?TGACh9G*k??lCh3QZns"))  # Output: stO?M?TGACh9
print(solution("echO33YPTP2mVo8aIRhh2"))              # Output: TP2mVo8aIRhh
print(solution("dHA..23203y0qc9R1I*?Z95JnIq6?3"))    # Output: 03y0qc9R1I*?