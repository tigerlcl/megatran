def solution(input):
    # Extract the components from the input string
    easting, northing, zone = input.split(', ')
    
    # Remove the 'mE' and 'mN' suffixes and convert to integers
    easting = int(easting[:-2])
    northing = int(northing[:-2])
    
    # Extract the zone number and letter
    zone_number = int(zone[:-1])
    zone_letter = zone[-1]
    
    # Calculate the latitude and longitude
    latitude = northing / 100000.0
    longitude = (easting / 100000.0) - (30 - zone_number)
    
    # Adjust longitude for the western hemisphere
    if zone_letter in 'CDEFGHJKLM':
        longitude = -longitude
    
    # Format the output as required
    output = f"{latitude:.2f}, {longitude:.2f}"
    
    return output