def solution(input):
    # Convert the input octal string to decimal
    try:
        decimal_value = int(input, 8)  # Convert from octal (base 8) to decimal (base 10)
        output = str(decimal_value)  # Convert the decimal value to string
    except ValueError:
        output = "Invalid octal number"  # Handle invalid input

    return output