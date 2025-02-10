import utm

def solution(input):
    # Parse the input string to extract latitude and longitude
    latitude, longitude = map(float, input.split(', '))
    
    # Convert latitude and longitude to UTM coordinates
    easting, northing, zone_number, zone_letter = utm.from_latlon(latitude, longitude)
    
    # Format the output string
    output = f"UTM Easting: {int(easting)}mE, UTM Northing: {int(northing)}mN, Zone: {zone_number}{zone_letter}"
    
    return output