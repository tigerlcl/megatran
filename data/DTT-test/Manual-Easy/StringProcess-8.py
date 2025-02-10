def solution(input):
    # Remove the outer curly braces and split the string by '}, {'
    tuples = input[2:-2].split('}, {')
    
    # Split the second tuple by comma and strip any extra spaces
    second_tuple = tuples[1].split(',')
    second_element = second_tuple[1].strip()
    
    return second_element