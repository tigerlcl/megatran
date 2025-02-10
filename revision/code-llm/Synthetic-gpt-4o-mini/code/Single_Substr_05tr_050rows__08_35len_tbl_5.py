def solution(input):
    # Find the last occurrence of a digit in the input string
    last_digit_index = -1
    for i in range(len(input)):
        if input[i].isdigit():
            last_digit_index = i
    
    # If a digit was found, slice the string from the character after the last digit to the end
    if last_digit_index != -1:
        output = input[last_digit_index + 1:]
    else:
        output = input  # If no digit is found, return the original input
    
    return output