def solution(input):
    # Split the input string into first name and last name
    first_name, last_name = input.split()
    # Get the first letter of the first name and concatenate with the last name
    output = f"{first_name[0]}. {last_name}"
    return output