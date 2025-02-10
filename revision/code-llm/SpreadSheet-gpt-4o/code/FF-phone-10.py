def solution(input):
    # Split the input into two parts: the country code and the rest of the number
    parts = input.split(' ', 1)
    country_code = parts[0]
    rest_of_number = parts[1]
    
    # Split the rest of the number into three parts
    first_part, second_part, third_part = rest_of_number.split('-')
    
    # Format the output as required
    output = f"{country_code} ({first_part}) {second_part}-{third_part}"
    
    return output