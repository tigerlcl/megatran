def solution(input):
    # Split the input into lines
    lines = input.splitlines()
    # Retain the first 3 characters from each line
    output = '\n'.join(line[:3] for line in lines)
    return output