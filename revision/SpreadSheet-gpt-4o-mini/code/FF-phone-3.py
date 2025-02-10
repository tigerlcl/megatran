def solution(input):
    # Split the input string by the hyphen
    parts = input.split('-')
    # Format the output with parentheses around the area code
    output = f"({parts[0]}) {parts[1]}-{parts[2]}"
    return output