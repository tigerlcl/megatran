def solution(input):
    def dms_to_decimal(degree_str):
        # Split the string into degrees, minutes, seconds and direction
        parts = degree_str[:-1].split('°')
        degrees = int(parts[0])
        minutes = int(parts[1].split("'")[0])
        seconds = int(parts[1].split("'")[1].split('"')[0])
        direction = degree_str[-1]
        
        # Calculate decimal degrees
        decimal_degrees = degrees + minutes / 60 + seconds / 3600
        
        # Adjust for direction
        if direction in ['S', 'W']:
            decimal_degrees *= -1
        
        return decimal_degrees

    # Split the input into latitude and longitude
    lat_str, lon_str = input.split(', ')
    
    # Convert both latitude and longitude to decimal
    latitude = dms_to_decimal(lat_str)
    longitude = dms_to_decimal(lon_str)
    
    # Format the output
    output = f"{latitude:.3f}, {longitude:.3f}"
    return output