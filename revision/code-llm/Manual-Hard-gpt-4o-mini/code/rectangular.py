def solution(input):
    # Remove parentheses and split the input string into two float values
    x, y = map(float, input.strip("()").split(", "))
    
    # Calculate the desired output values
    first_value = round(x + y)  # Round the sum of x and y
    second_value = int((y / (x + y)) * 90)  # Calculate the percentage of y in the sum and scale to 90
    
    # Return the output as a tuple in string format
    return f"({first_value}, {second_value})"