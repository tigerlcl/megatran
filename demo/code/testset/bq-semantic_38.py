from mgrs import MGRS

def solution(input):
    # Create an instance of the MGRS class
    mgrs = MGRS()
    
    # Convert the MGRS input to latitude and longitude
    lat, lon = mgrs.toLatLon(input)
    
    # Format the output to the required precision
    output = f"{lat:.5f}, {lon:.5f}"
    
    return output