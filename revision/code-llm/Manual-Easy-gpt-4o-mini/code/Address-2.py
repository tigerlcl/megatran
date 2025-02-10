def solution(input):
    # Split the input string by commas
    parts = input.split(',')
    # The city is the second part after splitting, strip any whitespace
    city = parts[1].strip()
    return city