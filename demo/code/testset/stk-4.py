def solution(input):
    # Use a set to get distinct characters
    distinct_characters = set(input)
    # Convert the set back to a string
    output = ''.join(distinct_characters)
    return output