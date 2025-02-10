def solution(input):
    # Extract the hexadecimal part of the input
    hex_value = input[2:]
    # Convert the hexadecimal to decimal and format it as a 3-digit string
    output = f"{int(hex_value, 16):03}"
    return output