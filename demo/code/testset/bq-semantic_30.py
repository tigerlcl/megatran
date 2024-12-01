import mgrs

def solution(input):
    # Split the input string to get latitude and longitude
    lat, lon = map(float, input.split(', '))
    
    # Create an MGRS object
    m = mgrs.MGRS()
    
    # Convert latitude and longitude to MGRS format
    output = m.toMGRS(lat, lon)
    
    return output