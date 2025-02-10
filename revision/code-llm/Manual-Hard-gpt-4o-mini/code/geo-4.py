from pyproj import Proj, transform

def solution(input):
    # Parse the input string to get latitude and longitude
    lat, lon = map(float, input.split(', '))
    
    # Define the UTM projection
    # UTM zone calculation
    zone_number = int((lon + 180) / 6) + 1
    is_northern = lat >= 0
    zone_letter = 'CDEFGHJKLMNPQRSTUVWXX'[int((lat + 80) / 8)]
    
    # Create the UTM projection
    proj_utm = Proj(proj='utm', zone=zone_number, northern=is_northern)
    
    # Transform the coordinates
    easting, northing = proj_utm(lon, lat)
    
    # Format the output
    output = f"UTM Easting: {int(easting)}mE, UTM Northing: {int(northing)}mN, Zone: {zone_number}{zone_letter}"
    
    return output