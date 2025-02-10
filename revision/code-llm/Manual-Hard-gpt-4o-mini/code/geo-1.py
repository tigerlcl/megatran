def solution(input):
    # Split the input into latitude and longitude
    lat_str, lon_str = input.split(', ')
    
    # Function to convert DMS to decimal
    def dms_to_decimal(dms_str):
        # Split the DMS string into degrees, minutes, seconds and direction
        parts = dms_str.split('°')
        degrees = float(parts[0])
        minutes = float(parts[1].split("'")[0])
        seconds = float(parts[1].split("'")[1][:-1])  # Remove the direction character
        
        # Convert to decimal
        decimal = degrees + minutes / 60 + seconds / 3600
        
        # Adjust for direction
        if 'S' in dms_str or 'W' in dms_str:
            decimal = -decimal
        
        return decimal
    
    # Convert both latitude and longitude
    latitude = dms_to_decimal(lat_str)
    longitude = dms_to_decimal(lon_str)
    
    # Format the output
    output = f"{latitude:.3f}, {longitude:.3f}"
    return output