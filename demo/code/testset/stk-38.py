def solution(input):
    # Split the input name into parts
    name_parts = input.split()
    
    # Get the first letter of the first name and the full last name
    first_initial = name_parts[0][0]
    last_name = name_parts[1]
    
    # Format the abbreviation
    output = f"{first_initial}. {last_name}"
    
    return output