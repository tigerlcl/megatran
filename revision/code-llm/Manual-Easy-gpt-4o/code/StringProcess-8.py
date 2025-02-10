def solution(input):
    # Remove the outer curly braces and split into sets
    sets = input.strip('{}').split('}, {')
    
    # Extract the second set
    second_set = sets[1]
    
    # Split the second set into individual elements
    elements = second_set.split(', ')
    
    # Return the second element of the second set
    return elements[1]