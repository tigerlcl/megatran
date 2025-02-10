def solution(input):
    # Split the input string into a list of words
    name_parts = input.split()
    
    # The first name is the first element of the list
    first_name = name_parts[0]
    
    # The initial of the last name is the first letter of the last element of the list
    last_initial = name_parts[-1][0]
    
    # Combine the first name with the last initial followed by a period
    output = f"{first_name} {last_initial}."
    
    return output