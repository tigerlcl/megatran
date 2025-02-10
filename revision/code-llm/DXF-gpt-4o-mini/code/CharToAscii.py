def solution(input):
    # Convert the input Unicode string to an integer
    unicode_value = int(input.split('+')[1], 16)
    # Format the integer as a three-digit string
    output = f"{unicode_value:03}"
    return output