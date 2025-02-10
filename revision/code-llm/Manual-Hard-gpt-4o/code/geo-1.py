def solution(input):
    def dms_to_decimal(degrees, minutes, seconds, direction):
        decimal = degrees + minutes / 60 + seconds / 3600
        if direction in ['S', 'W']:
            decimal = -decimal
        return round(decimal, 3)
    
    parts = input.split(', ')
    lat_dms = parts[0]
    lon_dms = parts[1]
    
    # Parse latitude
    lat_deg, lat_min, lat_sec_dir = lat_dms.split('°')
    lat_min, lat_sec_dir = lat_min.split("'")
    lat_sec = lat_sec_dir[:-1]
    lat_dir = lat_sec_dir[-1]
    
    # Parse longitude
    lon_deg, lon_min, lon_sec_dir = lon_dms.split('°')
    lon_min, lon_sec_dir = lon_min.split("'")
    lon_sec = lon_sec_dir[:-1]
    lon_dir = lon_sec_dir[-1]
    
    # Convert to decimal
    latitude = dms_to_decimal(int(lat_deg), int(lat_min), int(lat_sec), lat_dir)
    longitude = dms_to_decimal(int(lon_deg), int(lon_min), int(lon_sec), lon_dir)
    
    return f"{latitude}, {longitude}"