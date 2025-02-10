def solution(input):
    # Split the input into the country code and the rest of the number
    parts = input.split()
    country_code = parts[0]
    number = parts[1]
    
    # Split the number into the required parts
    number_parts = number.split('-')
    
    # Format the output
    output = f"{country_code} ({number_parts[0]}) {number_parts[1]}-{number_parts[2]}"
    
    return output