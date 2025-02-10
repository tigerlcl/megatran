def solution(input):
    # Split the input string into a list of words
    words = input.split()
    # Reverse the order of the words
    reversed_words = words[::-1]
    # Join the reversed words back into a single string
    output = ' '.join(reversed_words)
    return output