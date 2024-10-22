def solution(input):
    default_area_code = "425"
    
    # Split the input to check the format
    parts = input.split('-')
    
    # If the input has 3 parts, it already has an area code
    if len(parts) == 3:
        output = input
    else:
        # If it has 2 parts, prepend the default area code
        output = f"{default_area_code}-{input}"
    
    return output