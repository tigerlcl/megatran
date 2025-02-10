def solution(input):
    # Split the input string by the hyphen
    parts = input.split('-')
    # Extract the middle three digits (the second part)
    output = parts[1]
    return output