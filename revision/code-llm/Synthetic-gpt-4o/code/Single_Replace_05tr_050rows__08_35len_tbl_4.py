def solution(input):
    # Check if the input string contains 'Y'
    if 'Y' in input:
        # Find the index of the first occurrence of 'Y'
        index = input.index('Y')
        # Insert 'y' after the first 'Y'
        output = input[:index + 1] + 'y' + input[index + 1:]
    else:
        # If 'Y' is not found, return the input as is
        output = input
    return output