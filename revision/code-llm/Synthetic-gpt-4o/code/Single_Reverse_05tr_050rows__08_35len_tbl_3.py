def solution(input):
    # Reverse the entire input string
    reversed_input = input[::-1]
    # Split the reversed string into words
    words = reversed_input.split()
    # Reverse the order of the words
    output = ' '.join(words[::-1])
    return output