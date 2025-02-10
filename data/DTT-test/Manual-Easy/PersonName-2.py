def solution(input):
    # Split the input string into first name and last name
    last_name, first_name = input.split(', ')
    # Create the alias by combining the first letter of the first name with the last name
    alias = first_name[0] + last_name
    return alias