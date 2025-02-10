def solution(input):
    # Split the input string by hyphens
    parts = input.split('-')
    # The middle three digits are the second part of the split string
    middle_three_digits = parts[1]
    return middle_three_digits