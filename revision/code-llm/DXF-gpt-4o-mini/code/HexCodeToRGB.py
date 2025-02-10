def solution(input):
    # Remove the '#' character from the input
    hex_color = input.lstrip('#')
    
    # Convert the hex color to RGB values
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    
    # Combine the RGB values into a single integer
    output = (r * 1000000) + (g * 1000) + b
    
    return f"({output})"