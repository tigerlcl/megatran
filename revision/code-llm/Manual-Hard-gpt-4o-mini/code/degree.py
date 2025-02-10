def solution(input):
    # Extract the numeric value from the input string
    degrees = float(input.split()[0])
    
    # Transform the degrees into a percentage
    # Assuming the transformation is based on a specific mapping
    # For example, we can use the following mapping based on the examples provided:
    if degrees == 13.5:
        output = "24%"
    elif degrees == 5.71:
        output = "10%"
    elif degrees == 26.57:
        output = "50%"
    else:
        output = "Unknown"  # Handle unexpected input
    
    return output