import utm

def solution(input):
    # Split the input string to get latitude and longitude
    lat, lon = map(float, input.split(', '))
    
    # Convert to UTM
    easting, northing, zone_number, zone_letter = utm.from_latlon(lat, lon)
    
    # Format the output
    output = f"UTM Easting: {int(easting)}mE, UTM Northing: {int(northing)}mN, Zone: {zone_number}{zone_letter}"
    return output