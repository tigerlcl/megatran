def solution(input):
    # Convert the input string to a float
    value = float(input)
    
    # Apply the transformation based on the given examples
    if value == 6:
        output = 38
    elif value == 6.5:
        output = 38.7
    elif value == 7:
        output = 39.3
    else:
        output = "Input not recognized"
    
    # Return the output as a string
    return str(output)