def solution(input):
    # Split the input string to extract the second set of elements
    elements = input.split('}, {')
    
    # Remove the curly braces and split the second set into individual elements
    second_set = elements[1].replace('{', '').replace('}', '').split(', ')
    
    # Return the first element of the second set
    output = second_set[0]
    return output