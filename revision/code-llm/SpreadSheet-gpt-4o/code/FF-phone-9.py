def solution(input):
    # Remove the leading '+' and replace '-' with '.'
    output = input[1:].replace('-', '.').replace(' ', '.')
    return output