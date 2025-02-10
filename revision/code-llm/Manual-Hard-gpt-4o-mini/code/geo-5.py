def solution(input):
    import utm
    
    # Split the input string into components
    easting, northing, zone = input.split(', ')
    
    # Extract the numeric values and convert them to float
    easting_value = float(easting[:-2])  # Remove 'mE'
    northing_value = float(northing[:-2])  # Remove 'mN'
    
    # Extract the zone number and letter
    zone_number = int(zone[:-1])  # Remove the letter
    zone_letter = zone[-1]  # Get the letter
    
    # Convert UTM to latitude and longitude
    latitude, longitude = utm.to_latlon(easting_value, northing_value, zone_number, zone_letter)
    
    # Format the output to two decimal places
    output = f"{latitude:.2f}, {longitude:.2f}"
    
    return output