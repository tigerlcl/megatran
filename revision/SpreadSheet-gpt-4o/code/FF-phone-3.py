def solution(input):
    # Split the input string into parts
    parts = input.split('-')
    # Format the phone number with parentheses around the area code
    output = f"({parts[0]}) {parts[1]}-{parts[2]}"
    return output