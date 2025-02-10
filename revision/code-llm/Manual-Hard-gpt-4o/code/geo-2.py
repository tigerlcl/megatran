def solution(input):
    import math
    
    # Split the input string into components
    parts = input.split()
    
    # Extract the zone, hemisphere, easting, and northing
    zone_number = int(parts[0][:-1])
    hemisphere = parts[0][-1]
    easting = int(parts[2])
    northing = int(parts[4])
    
    # Constants for UTM to Lat/Lon conversion
    k0 = 0.9996
    e = 0.00669438
    e1sq = e / (1 - e)
    a = 6378137  # Radius of the Earth in meters
    
    # Calculate the longitude origin of the zone
    lon_origin = (zone_number - 1) * 6 - 180 + 3
    
    # Adjust northing for southern hemisphere
    if hemisphere == 'S':
        northing -= 10000000
    
    # Calculate the footpoint latitude
    m = northing / k0
    mu = m / (a * (1 - e / 4 - 3 * e**2 / 64 - 5 * e**3 / 256))
    
    # Calculate latitude
    e1 = (1 - (1 - e)**0.5) / (1 + (1 - e)**0.5)
    j1 = 3 * e1 / 2 - 27 * e1**3 / 32
    j2 = 21 * e1**2 / 16 - 55 * e1**4 / 32
    j3 = 151 * e1**3 / 96
    j4 = 1097 * e1**4 / 512
    fp_lat = mu + j1 * math.sin(2 * mu) + j2 * math.sin(4 * mu) + j3 * math.sin(6 * mu) + j4 * math.sin(8 * mu)
    
    # Calculate latitude and longitude
    c1 = e1sq * math.cos(fp_lat)**2
    t1 = math.tan(fp_lat)**2
    r1 = a * (1 - e) / (1 - e * math.sin(fp_lat)**2)**1.5
    n1 = a / (1 - e * math.sin(fp_lat)**2)**0.5
    d = (easting - 500000) / (n1 * k0)
    
    q1 = n1 * math.tan(fp_lat) / r1
    q2 = (d**2 / 2)
    q3 = (5 + 3 * t1 + 10 * c1 - 4 * c1**2 - 9 * e1sq) * d**4 / 24
    q4 = (61 + 90 * t1 + 298 * c1 + 45 * t1**2 - 252 * e1sq - 3 * c1**2) * d**6 / 720
    lat = fp_lat - q1 * (q2 - q3 + q4)
    
    q5 = d
    q6 = (1 + 2 * t1 + c1) * d**3 / 6
    q7 = (5 - 2 * c1 + 28 * t1 - 3 * c1**2 + 8 * e1sq + 24 * t1**2) * d**5 / 120
    lon = lon_origin + (q5 - q6 + q7) / math.cos(fp_lat)
    
    # Convert latitude and longitude from radians to degrees
    lat = lat * 180 / math.pi
    lon = lon * 180 / math.pi
    
    # Format the output
    output = f"{lat:.3f}, {lon:.3f}"
    return output