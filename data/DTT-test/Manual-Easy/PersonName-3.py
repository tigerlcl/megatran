def solution(input):
    # Split the input string by tabs
    parts = input.split('\t')
    
    # Rearrange and format the components
    last_name = parts[0]
    middle_initial = parts[1]
    first_name = parts[2]
    
    # Create the formatted output string
    output = f"{last_name}, {first_name} {middle_initial}."
    
    return output