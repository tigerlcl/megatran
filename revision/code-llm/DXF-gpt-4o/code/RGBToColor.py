def solution(input):
    # Split the input string by semicolons to get the RGB values
    r, g, b = map(int, input.split(';'))
    
    # Define a dictionary to map RGB values to color names
    color_map = {
        (84, 84, 84): "Grey",
        (211, 211, 211): "LightGrey",
        (255, 255, 255): "White"
    }
    
    # Return the corresponding color name from the dictionary
    return color_map.get((r, g, b), "Unknown")