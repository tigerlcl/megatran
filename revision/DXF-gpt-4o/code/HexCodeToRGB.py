def solution(input):
    # Remove the '#' character from the input
    hex_color = input.lstrip('#')
    
    # Convert each component from hexadecimal to decimal
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    
    # Concatenate the decimal values as strings and convert to an integer
    rgb_integer = int(f"{r}{g}{b}")
    
    # Return the result as a tuple
    return (rgb_integer,)

# Example usage:
# print(solution("#ffb6c1"))  # Output: (255182193)
# print(solution("#333333"))  # Output: (515151)
# print(solution("#d52b1e"))  # Output: (2134330)