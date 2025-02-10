def solution(input):
    # Convert the input string to a float
    fahrenheit = float(input)
    
    # Convert Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * 5.0/9.0
    
    # Format the output to 2 decimal places
    output = f"{celsius:.2f}"
    
    return output