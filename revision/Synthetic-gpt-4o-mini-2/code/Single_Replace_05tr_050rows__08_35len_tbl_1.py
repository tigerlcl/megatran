def solution(input):
    # Remove all special characters and retain only A-Z, a-z, 0-9, and spaces
    output = ''.join(char for char in input if char.isalnum() or char.isspace())
    return output