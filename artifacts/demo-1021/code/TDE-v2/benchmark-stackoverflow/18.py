def solution(input):
    # Split the input string into words
    words = input.split()
    # Capitalize the first letter of each word and join them together
    output = ''.join(word.capitalize() for word in words)
    return output