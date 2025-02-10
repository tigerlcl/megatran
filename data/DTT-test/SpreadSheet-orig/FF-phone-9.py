def solution(input):
    # Remove special characters except for digits and spaces
    cleaned = ''.join(char for char in input if char.isdigit() or char.isspace())
    # Split the cleaned string into parts based on spaces
    parts = cleaned.split()
    # Join the parts with dots
    output = '.'.join(parts)
    return output