def solution(input):
    # Split the input string into parts
    parts = input.split()
    
    # Extract the country code and the phone number
    country_code = parts[0]
    phone_number = parts[1]
    
    # Split the phone number into area code and the rest
    area_code, rest_of_number = phone_number.split('-', 1)
    
    # Format the output
    output = f"{country_code} ({area_code}) {rest_of_number.replace('-', '-')}"
    
    return output