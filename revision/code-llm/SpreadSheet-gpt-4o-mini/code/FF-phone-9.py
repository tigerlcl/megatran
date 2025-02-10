def solution(input):
    # Remove the leading '+' and any spaces
    cleaned_input = input.replace('+', '').replace(' ', '')
    
    # Replace '-' with '.' to format the output correctly
    output = cleaned_input.replace('-', '.')
    
    return output