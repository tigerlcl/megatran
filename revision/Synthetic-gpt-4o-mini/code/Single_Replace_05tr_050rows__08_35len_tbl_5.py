def solution(input):
    # Define the characters to be replaced with underscores
    characters_to_replace = [' ']
    
    # Replace specified characters with underscores
    output = input
    for char in characters_to_replace:
        output = output.replace(char, '_')
    
    return output