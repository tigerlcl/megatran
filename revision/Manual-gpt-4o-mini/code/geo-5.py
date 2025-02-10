import utm

def solution(input):
    # Split the input string into its components
    easting, northing, zone = input.split(', ')
    
    # Remove the 'mE' and 'mN' suffixes and convert to float
    easting = float(easting[:-2])
    northing = float(northing[:-2])
    
    # Convert UTM to latitude and longitude
    latitude, longitude = utm.to_latlon(easting, northing, int(zone[:-1]), zone[-1])
    
    # Format the output to 2 decimal places
    output = f"{latitude:.2f}, {longitude:.2f}"
    return output