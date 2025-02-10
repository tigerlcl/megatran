def solution(input):
    if len(input) < 2:
        return input  # If the string is too short, return it as is
    
    last_char = input[-1]
    second_last_char = input[-2]
    
    if last_char != second_last_char:
        output = input[:-1] + second_last_char  # Replace last character with the second last
    else:
        output = input  # No change if the last two characters are the same
    
    return output