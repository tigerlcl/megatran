def solution(input):
    # Split the input name into parts
    parts = input.split()
    # Get the first initial and the last name
    abbreviation = f"{parts[0][0]}. {parts[-1]}"
    return abbreviation