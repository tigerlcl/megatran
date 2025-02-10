def solution(input):
    # Split the input string by commas
    parts = input.split(',')
    # The city is the second part, strip any leading/trailing whitespace
    city = parts[1].strip()
    return city