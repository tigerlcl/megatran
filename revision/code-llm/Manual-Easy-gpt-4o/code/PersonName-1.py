def solution(input):
    # Split the input string by tab character
    parts = input.split('\t')
    # Take the first character of the first part and concatenate with the second part
    output = parts[0][0] + parts[1]
    return output