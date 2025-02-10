def solution(input):
    # Split the input string into first name and last name
    first_name, last_name = input.split()
    # Create the desired output format
    output = f"{first_name[0]}. {last_name}"
    return output