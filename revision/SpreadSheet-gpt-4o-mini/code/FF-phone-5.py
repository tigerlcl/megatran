def solution(input):
    # Split the input string by spaces and take the first part
    country_code = input.split()[0]
    # Remove the '+' sign from the country code
    output = country_code[1:]
    return output