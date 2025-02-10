def solution(input):
    # Remove the '#' from the input
    hex_value = input.lstrip('#')
    
    # Convert each pair of hex digits to decimal and concatenate them
    r = int(hex_value[0:2], 16)
    g = int(hex_value[2:4], 16)
    b = int(hex_value[4:6], 16)
    
    # Concatenate the decimal values as a string
    output = f"({r}{g}{b})"
    
    return output