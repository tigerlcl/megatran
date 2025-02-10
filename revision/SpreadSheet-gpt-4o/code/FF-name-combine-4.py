def solution(input):
    # Split the input string by spaces
    parts = input.split()
    # Extract the last name and the first initial
    last_name = parts[-1]
    first_initial = parts[0][0]
    # Format the output as 'LastName- FirstInitial.'
    output = f"{last_name}- {first_initial}."
    return output