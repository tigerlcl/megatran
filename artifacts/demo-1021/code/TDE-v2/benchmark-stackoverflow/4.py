def solution(input):
    # Use a set to get distinct characters
    distinct_characters = set(input)
    # Join the distinct characters to form the output string
    output = ''.join(distinct_characters)
    return output