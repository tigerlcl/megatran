def solution(input):
    # Extract the numeric value from the input string
    degrees = float(input.split()[0])
    
    # Convert degrees to percentage
    percentage = int(degrees / 26.57 * 50)
    
    # Format the output string
    output = f"{percentage}%"
    
    return output