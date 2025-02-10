def solution(input):
    # Remove any parentheses and spaces
    cleaned_input = input.replace('(', '').replace(')', '').replace(' ', '')
    
    # Check if the input contains a dash
    if '-' in cleaned_input:
        # Split the input by dash
        parts = cleaned_input.split('-')
        # Format the output
        output = f"{parts[0]}-{parts[1][:3]}-{parts[1][3:]}"
    else:
        # If no dash, assume it's a full number
        area_code = cleaned_input[:3]
        local_number = cleaned_input[3:]
        output = f"{area_code}-{local_number[:3]}-{local_number[3:]}"
    
    return output