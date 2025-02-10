def solution(input):
    # Split the input string into a list of words
    words = input.split()
    # Extract the first letter of each word and join them with a dot
    initials = '.'.join(word[0] for word in words)
    # Add a dot at the end
    output = initials + '.'
    return output