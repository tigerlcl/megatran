def solution(input):
    import mgrs
    
    # Parse the input string to extract latitude and longitude
    lat_str, lon_str = input.split(', ')
    latitude = float(lat_str)
    longitude = float(lon_str)
    
    # Initialize the MGRS converter
    m = mgrs.MGRS()
    
    # Convert latitude and longitude to MGRS
    mgrs_code = m.toMGRS(latitude, longitude)
    
    return mgrs_code

# Example usage:
# print(solution("23.11, -39.33"))  # Output: 24QVL6620855735