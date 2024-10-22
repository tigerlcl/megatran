def solution(input):
    # Convert input string to float
    fahrenheit = float(input)
    # Convert Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    # Round the result
    rounded_celsius = round(celsius)
    # Convert the result back to string
    output = str(rounded_celsius)
    return output