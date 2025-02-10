def solution(input):
    # Split the input string by space to separate the country code and the rest of the number
    parts = input.split(' ')
    # Split the rest of the number by '-' and get the first part
    area_code = parts[1].split('-')[0]
    return area_code