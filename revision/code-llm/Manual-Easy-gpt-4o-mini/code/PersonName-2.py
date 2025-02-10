def solution(input):
    # Split the input string into two names
    first_name, second_name = input.split(', ')
    
    # Get the first character of the second name
    first_char_second_name = second_name[0]
    
    # Concatenate the first character of the second name with the first name
    output = first_char_second_name + first_name
    
    return output