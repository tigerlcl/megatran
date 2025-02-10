def solution(input):
    # Split the input string into words
    names = input.split()
    # Extract the first letter of each name and join them with a dot
    initials = '.'.join(name[0] for name in names)
    # Format the output with dots and return
    output = initials + '.'
    return output