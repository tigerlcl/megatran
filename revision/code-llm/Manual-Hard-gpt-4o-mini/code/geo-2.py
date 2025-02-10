def solution(input):
    # Mapping of grid zones to their respective latitude offsets
    lat_lon_offsets = {
        'S': -1, 'N': 1, 'C': 0, 'J': 0, 'Q': 0, 'T': 0
    }
    
    # Split the input into components
    parts = input.split()
    lat_zone = parts[0][-1]  # Last character of the first part indicates latitude zone
    lon_zone = parts[1]       # Second part indicates longitude zone
    northing = int(parts[2])  # Third part is the northing value
    easting = int(parts[4])   # Fifth part is the easting value

    # Calculate latitude and longitude based on the zone and offsets
    latitude = lat_lon_offsets[lat_zone] * (northing / 1000000.0)
    longitude = (easting / 1000000.0) * (1 if lon_zone == 'E' else -1)

    # Format the output to three decimal places
    output = f"{latitude:.3f}, {longitude:.3f}"
    return output