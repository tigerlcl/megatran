def solution(input):
    # Split the input string into first and last name
    names = input.split()
    # Get the first name and last name
    first_name = names[0]
    last_name = names[1]
    # Create the abbreviation for the first name and concatenate with the last name
    output = f"{first_name[0]}. {last_name}"
    return output