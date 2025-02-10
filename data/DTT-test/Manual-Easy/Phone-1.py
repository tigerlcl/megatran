def solution(input):
    # Extract the area code, central office code, and station code
    area_code = input[:3]
    central_office_code = input[3:6]
    station_code = input[6:]
    
    # Format the phone number
    output = f"({area_code}) {central_office_code}-{station_code}"
    
    return output