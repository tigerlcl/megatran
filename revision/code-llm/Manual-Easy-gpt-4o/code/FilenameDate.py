def solution(input):
    # Split the input string by underscore
    parts = input.split('_')
    
    # Extract the month and year
    month = parts[0]
    year = parts[1]
    
    # Format the output as required
    output = f"{month}/01/{year}"
    
    return output