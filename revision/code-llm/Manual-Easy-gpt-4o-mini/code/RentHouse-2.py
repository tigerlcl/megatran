def solution(input):
    # Split the input string by spaces
    parts = input.split()
    
    # Find the part that contains the price, which is prefixed by a dollar sign
    for part in parts:
        if part.startswith('$'):
            # Return the price without the dollar sign
            return part[1:]
    
    # If no price is found, return an empty string (or handle as needed)
    return ""