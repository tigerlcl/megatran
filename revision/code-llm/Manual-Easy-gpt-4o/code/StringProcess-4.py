def solution(input):
    # Remove punctuation from the input string
    output = ''.join(char for char in input if char.isalnum() or char.isspace())
    return output