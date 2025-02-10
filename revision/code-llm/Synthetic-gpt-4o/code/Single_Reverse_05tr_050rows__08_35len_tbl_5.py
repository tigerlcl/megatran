def solution(input):
    # Reverse the entire input string
    reversed_input = input[::-1]
    # Split the reversed string into words
    words = reversed_input.split()
    # Reverse the order of words to maintain the original word order
    words.reverse()
    # Join the words with a space to form the final output
    output = ' '.join(words)
    return output