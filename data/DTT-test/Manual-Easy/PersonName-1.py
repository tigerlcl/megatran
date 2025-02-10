def solution(input):
    # Split the input string by tab character to get the two names
    first_name, last_name = input.split('\t')
    # Create the alias by taking the first letter of the first name and appending the last name
    alias = first_name[0] + last_name
    return alias