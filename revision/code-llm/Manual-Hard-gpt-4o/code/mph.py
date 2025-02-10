def solution(input):
    # Convert the input string to a float
    kmh = float(input)
    
    # Convert km/h to m/s by dividing by 3.6
    ms = kmh / 3.6
    
    # Format the result to two decimal places and append ' m/s'
    output = f"{ms:.2f} m/s"
    
    return output