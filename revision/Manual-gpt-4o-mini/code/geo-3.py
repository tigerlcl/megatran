def solution(input):
    import pyproj

    # Define the MGRS to WGS84 transformation
    mgrs = pyproj.Proj(proj='utm', zone=int(input[0:2]), ellps='WGS84', south=False)
    lat, lon = mgrs(input[3:9], input[9:15], inverse=True)

    # Format the output to 3 decimal places
    output = f"{lat:.3f}, {lon:.3f}"
    return output