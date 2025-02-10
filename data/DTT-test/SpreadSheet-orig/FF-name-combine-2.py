def solution(input):
    # Split the input name into parts
    parts = input.split()
    # Get the first part (first name) and the first letter of the second part (last name)
    output = f"{parts[0]} {parts[1][0]}."
    return output