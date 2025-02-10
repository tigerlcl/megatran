def solution(input):
    # Split the input string by the dash character
    parts = input.split('-')
    # The desired output is the last part of the split string
    output = parts[-1]
    return output