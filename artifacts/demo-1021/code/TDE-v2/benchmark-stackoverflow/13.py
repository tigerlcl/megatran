def solution(input):
    # Convert the input string to a float
    number = float(input)
    
    # Format the number with commas and two decimal places
    output = "{:,.2f}".format(number)
    
    return output