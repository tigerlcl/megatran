def solution(input):
    # Split the input string into two parts
    first_name, second_name = input.split('\t')
    
    # Take the first character of the first name
    first_char = first_name[0]
    
    # Concatenate the first character with the second name
    output = first_char + second_name
    
    return output