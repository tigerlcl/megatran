def solution(input):
    # Remove the outer curly braces and split the input string into rows
    rows = input.strip('{}').split('}, {')
    
    # Split the second row into elements
    second_row = rows[1].split(', ')
    
    # Get the second element of the second row
    output = second_row[1]
    
    return output