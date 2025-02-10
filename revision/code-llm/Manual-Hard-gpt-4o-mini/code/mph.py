def solution(input):
    # Convert the input string to a float
    value = float(input)
    
    # Calculate the output using the formula
    output_value = (value / 2.0) ** 0.5 * 9.81  # converting to m/s
    output = f"{output_value:.2f} m/s"  # format the output to 2 decimal places
    
    return output