def solution(input):
    # Split the input name into parts
    parts = input.split()
    # Get the first name and the first letter of the last name
    first_name = parts[0]
    last_initial = parts[1][0] + '.'
    # Format the output
    output = f"{first_name} {last_initial}"
    return output