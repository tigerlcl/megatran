def solution(input):
    # Convert the input string to an integer
    num = int(input)
    
    # Apply the transformation logic
    output = round(num * 0.45, 2)
    
    # Convert the output to string and return
    return str(output)