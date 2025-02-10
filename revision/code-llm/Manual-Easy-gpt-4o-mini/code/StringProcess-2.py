def solution(input):
    # Split the input string by semicolons to separate the groups
    groups = input.split(';')
    
    # For each group, split by commas and get the second group (index 1)
    second_group = groups[1].split(',')
    
    # Strip whitespace from each item in the second group
    second_group = [item.strip() for item in second_group]
    
    # Return the first item from the second group
    output = second_group[0]
    return output