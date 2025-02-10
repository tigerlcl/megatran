def solution(input):
    # Split the input string by spaces and hyphens
    parts = input.split()
    last_part = parts[-1].split('-')[-1]  # Get the last part after the last hyphen
    return last_part  # Return the last three digits of the phone number