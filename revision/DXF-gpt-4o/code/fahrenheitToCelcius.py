def solution(input):
    # Convert the input string to a float
    fahrenheit = float(input)
    
    # Convert Fahrenheit to Celsius using the formula
    celsius = (fahrenheit - 32) * 5 / 9
    
    # Format the output to two decimal places
    output = f"{celsius:.2f}"
    
    return output