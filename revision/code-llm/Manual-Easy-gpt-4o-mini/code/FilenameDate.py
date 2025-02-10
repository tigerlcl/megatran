def solution(input):
    # Split the input string by underscores
    parts = input.split('_')
    
    # Extract the month and year
    month = parts[0]
    year = parts[1]
    
    # Format the output as "MM/01/YYYY"
    output = f"{month}/01/{year}"
    
    return output