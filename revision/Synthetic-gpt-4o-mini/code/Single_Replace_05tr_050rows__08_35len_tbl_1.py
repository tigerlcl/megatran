def solution(input):
    # Remove surrounding parentheses from the beginning and end of the string
    while input and (input.startswith('(') or input.endswith(')')):
        if input.startswith('('):
            input = input[1:]
        if input.endswith(')'):
            input = input[:-1]
    return input