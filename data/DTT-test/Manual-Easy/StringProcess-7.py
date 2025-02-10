def solution(input):
    # Remove the outer curly braces and split the string into tuples
    tuples = input[2:-2].split('}, {')
    
    # Extract the second tuple and split it by comma
    second_tuple = tuples[1].split(', ')
    
    # Extract the second element from the second tuple
    output = second_tuple[1]
    
    return output