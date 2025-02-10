def solution(input):
    # Split the input string by spaces and take the first part
    # Remove the '+' sign and return the country code
    output = input.split()[0][1:]
    return output