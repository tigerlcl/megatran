def solution(input):
    # Split the input string by tab characters
    parts = input.split('\t')
    
    # Extract the last name, first initial, and first name
    last_name = parts[0]
    first_initial = parts[1]
    first_name = parts[2]
    
    # Format the output string
    output = f"{last_name}, {first_name} {first_initial}."
    
    return output