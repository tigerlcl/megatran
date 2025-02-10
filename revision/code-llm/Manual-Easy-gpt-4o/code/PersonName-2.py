def solution(input):
    # Split the input string into two parts
    last_name, first_name = input.split(", ")
    # Concatenate the first letter of the first name with the last name
    output = first_name[0] + last_name
    return output