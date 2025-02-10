def solution(input):
    # Check if the input string contains the character 'y'
    if 'y' not in input:
        # If 'y' is not present, append 'y' after the first character
        output = input[0] + 'y' + input[1:]
    else:
        # If 'y' is already present, return the input as is
        output = input
    return output