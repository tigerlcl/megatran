def solution(input):
    # Split the input string into parts
    parts = input.split()
    
    # Get the first letter of the first name and capitalize it
    first_initial = parts[0][0].upper()
    
    # Get the last name
    last_name = parts[1]
    
    # Format the abbreviation
    output = f"{first_initial}. {last_name}"
    
    return output