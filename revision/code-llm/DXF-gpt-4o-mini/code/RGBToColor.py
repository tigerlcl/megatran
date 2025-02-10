def solution(input):
    # Split the input string by semicolon and convert to integers
    r, g, b = map(int, input.split(';'))
    
    # Determine the color based on the RGB values
    if r == g == b:
        if r == 84:
            output = "Grey"
        elif r == 211:
            output = "LightGrey"
        elif r == 255:
            output = "White"
        else:
            output = "Unknown Color"
    else:
        output = "Not a shade of Grey"
    
    return output