def solution(input):
    # Extract distinct characters from the input string
    output = ''.join(sorted(set(input), key=input.index))
    return output