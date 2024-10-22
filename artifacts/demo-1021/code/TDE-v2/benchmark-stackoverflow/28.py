def solution(input):
    # Remove special characters and retain only A-Z, a-z, 0-9
    output = ''.join(char for char in input if char.isalnum())
    return output