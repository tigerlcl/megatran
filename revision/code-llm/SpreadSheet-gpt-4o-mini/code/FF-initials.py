def solution(input):
    # Split the input string into words
    names = input.split()
    # Extract the first letter of each name and concatenate them with a dot
    output = '.'.join(name[0] for name in names) + '.'
    return output