def solution(input):
    # Convert the input string to an integer
    input_number = int(input)
    
    # Apply the transformation formula
    output_number = input_number * 0.45
    
    # Format the output to two decimal places
    output = f"{output_number:.2f}"
    
    return output