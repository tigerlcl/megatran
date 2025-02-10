def solution(input):
    # Split the input string into first and last name
    first_name, last_name = input.split()
    
    # Create the output in the desired format
    output = f"{last_name}- {first_name[0]}."
    
    return output