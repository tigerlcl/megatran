def solution(input):
    # Split the input string into the base name and the numeric part
    output = ''.join(filter(str.isalpha, input))
    return output