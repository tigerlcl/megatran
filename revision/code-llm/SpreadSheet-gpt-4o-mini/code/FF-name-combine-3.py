def solution(input):
    # Split the input string into first and last name
    first_name, last_name = input.split()
    # Format the output as required
    output = f"{first_name[0]}. {last_name}"
    return output