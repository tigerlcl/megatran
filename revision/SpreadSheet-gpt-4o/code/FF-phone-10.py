def solution(input):
    # Split the input into country code and the rest of the phone number
    parts = input.split(' ', 1)
    country_code = parts[0]
    rest_of_number = parts[1]
    
    # Split the rest of the number into area code and the remaining part
    area_code, remaining_number = rest_of_number.split('-', 1)
    
    # Format the phone number
    output = f"{country_code} ({area_code}) {remaining_number}"
    
    return output