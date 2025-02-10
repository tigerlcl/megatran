def solution(input):
    # Add hyphens to the 9-digit Social Security Number
    output = input[:3] + '-' + input[3:6] + '-' + input[6:]
    return output