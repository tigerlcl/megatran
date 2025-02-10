def solution(input):
    # Remove the '+' at the beginning and split the string by space
    parts = input[1:].split(' ')
    # The first part is the country code
    country_code = parts[0]
    return country_code