import math

def solution(input):
    # Parse the input string to extract the two numbers
    input = input.strip("()")
    a, b = map(int, input.split(", "))
    
    # Calculate the results
    result1 = round(math.sqrt(a**2 - (a * math.cos(math.radians(b)))**2), 5)
    result2 = round(a * math.sin(math.radians(b)), 5)
    
    # Format the output as a tuple
    output = (result1, result2)
    
    return output