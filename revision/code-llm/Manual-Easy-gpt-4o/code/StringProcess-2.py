def solution(input):
    # Split the input string by semicolons to get the groups
    groups = input.split(';')
    
    # Get the second group (index 1) and strip any leading/trailing whitespace
    second_group = groups[1].strip()
    
    # Split the second group by commas to get the individual elements
    elements = second_group.split(',')
    
    # Get the first element of the second group and strip any leading/trailing whitespace
    output = elements[0].strip()
    
    return output