def solution(input):
    # Define a dictionary mapping RGB tuples to color names
    color_map = {
        (84, 84, 84): "Grey",
        (211, 211, 211): "LightGrey",
        (255, 255, 255): "White",
        # Add more mappings as needed
    }
    
    # Parse the input string into a tuple of integers
    rgb_values = tuple(map(int, input.split(';')))
    
    # Return the corresponding color name or a default value if not found
    return color_map.get(rgb_values, "Unknown")

# Example usage:
# print(solution("84;84;84"))  # Output: Grey
# print(solution("211;211;211"))  # Output: LightGrey
# print(solution("255;255;255"))  # Output: White