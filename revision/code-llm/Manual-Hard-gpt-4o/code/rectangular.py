import math

def solution(input):
    # Parse the input string to extract the two float values
    num1, num2 = map(float, input.strip("()").split(", "))
    
    # Calculate the sum of the two numbers and round it up to the nearest integer
    sum_rounded = math.ceil(num1 + num2)
    
    # Calculate the angle in degrees based on the difference between the two numbers
    angle = abs(num1 - num2) * 15
    
    # Format the output as a tuple
    output = (sum_rounded, int(angle))
    
    return output