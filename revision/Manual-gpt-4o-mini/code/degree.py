import math

def solution(input):
    # Extract the angle in degrees from the input string
    angle_degrees = float(input.split()[0])
    
    # Convert degrees to radians
    angle_radians = angle_degrees * (math.pi / 180)
    
    # Calculate the slope percentage
    slope_percentage = round(math.tan(angle_radians) * 100)
    
    # Format the output as a percentage string
    output = f"{slope_percentage}%"
    
    return output