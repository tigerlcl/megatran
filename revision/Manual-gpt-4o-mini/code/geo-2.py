def solution(input):
    import re

    # Define the grid reference pattern
    pattern = r'(\d{1,2}[NS])\s([A-Z])\s(\d{6})\s([A-Z])\s(\d{7})'
    match = re.match(pattern, input)

    if not match:
        return "Invalid input format"

    # Extract the components from the input
    grid_zone = match.group(1)
    grid_letter = match.group(2)
    easting = int(match.group(3))
    northing = int(match.group(5))

    # Define the constants for the conversion
    lat_offset = {
        'N': 0,
        'S': -90
    }
    
    lon_offset = {
        'A': -180,
        'B': -174,
        'C': -168,
        'D': -162,
        'E': -156,
        'F': -150,
        'G': -144,
        'H': -138,
        'J': -132,
        'K': -126,
        'L': -120,
        'M': -114,
        'N': -108,
        'P': -102,
        'Q': -96,
        'R': -90,
        'S': -84,
        'T': -78,
        'U': -72,
        'V': -66,
        'W': -60,
        'X': -54,
        'Y': -48,
        'Z': -42
    }

    # Calculate latitude and longitude
    lat = (northing / 1000000) * 180 - 90 + lat_offset[grid_zone[-1]]
    lon = (easting / 1000000) * 360 - 180 + lon_offset[grid_letter]

    # Format the output to 3 decimal places
    output = f"{lat:.3f}, {lon:.3f}"
    return output