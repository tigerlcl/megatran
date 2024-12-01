def solution(input):
    # Split the input name into parts
    parts = input.split()
    
    # Get the first initial and the last name
    first_initial = parts[0][0] + '.'
    last_name = parts[-1]
    
    # Format the output
    output = f"{first_initial} {last_name}"
    return output