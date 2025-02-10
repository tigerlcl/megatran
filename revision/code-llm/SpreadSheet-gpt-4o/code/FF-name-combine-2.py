def solution(input):
    # Split the input string into words
    parts = input.split()
    # The first name is the first word
    first_name = parts[0]
    # The initial of the last name is the first letter of the last word
    last_initial = parts[-1][0]
    # Combine the first name and the initial with a period
    output = f"{first_name} {last_initial}."
    return output