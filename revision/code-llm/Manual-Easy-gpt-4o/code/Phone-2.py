def solution(input):
    # Remove any parentheses and split the input by hyphen or space
    input = input.replace('(', '').replace(')', '').replace(' ', '-')
    
    # Ensure the input is split correctly
    if '-' not in input:
        input = input[:3] + '-' + input[3:6] + '-' + input[6:]
    elif input.count('-') == 1:
        input = input[:7] + '-' + input[7:]
    
    return input