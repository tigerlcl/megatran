def solution(input):
    output = ''
    for char in input:
        if char.isupper() and output:  # Check if the character is uppercase and output is not empty
            output += ' '  # Add a space before the uppercase character
        output += char  # Add the character to the output
    return output