def solution(input):
    # Split the input string into a list of words
    names = input.split()
    # Extract the first letter of each word and capitalize it
    initials = [name[0].upper() for name in names]
    # Join the initials with a dot
    output = '.'.join(initials) + '.'
    return output