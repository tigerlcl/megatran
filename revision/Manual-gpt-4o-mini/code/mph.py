def solution(input):
    # Convert the input string to a float
    mph = float(input)
    # Convert miles per hour to meters per second
    mps = mph * 0.44704
    # Format the output to two decimal places
    output = f"{mps:.2f} m/s"
    return output