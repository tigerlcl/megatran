def solution(input):
    # Remove the outer curly braces and split the string by '}, {'
    tuples = input.strip('{}').split('}, {')
    
    # Get the second tuple and split it by ', '
    second_tuple = tuples[1].split(', ')
    
    # Extract the first element of the second tuple
    output = second_tuple[0]
    
    return output