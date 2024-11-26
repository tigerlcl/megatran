def solution(input):
    import mgrs
    
    # Parse the input string to extract latitude and longitude
    lat_str, lon_str = input.split(',')
    latitude = float(lat_str.strip())
    longitude = float(lon_str.strip())
    
    # Create an MGRS object
    m = mgrs.MGRS()
    
    # Convert latitude and longitude to MGRS
    mgrs_result = m.toMGRS(latitude, longitude)
    
    return mgrs_result

# Example usage:
# print(solution("23.11, -39.33"))  # Output: 24QVL6620855735
# print(solution("44.11, -77.33"))  # Output: 18TUP1353886730
# print(solution("66.99, -33.11"))  # Output: 25WDQ9520130269