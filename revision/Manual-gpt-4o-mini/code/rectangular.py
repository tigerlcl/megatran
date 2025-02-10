import math

def solution(input):
    # Parse the input string to get the rectangular coordinates
    x, y = map(float, input.strip("()").split(", "))
    
    # Calculate the radius (r) and angle (theta) in degrees
    r = math.sqrt(x**2 + y**2)
    theta = math.degrees(math.atan2(y, x))
    
    # Normalize the angle to be in the range [0, 360)
    if theta < 0:
        theta += 360
    
    # Round the radius and angle to the nearest integer
    r_rounded = round(r)
    theta_rounded = round(theta)
    
    # Format the output as a string
    output = f"({r_rounded}, {theta_rounded})"
    return output