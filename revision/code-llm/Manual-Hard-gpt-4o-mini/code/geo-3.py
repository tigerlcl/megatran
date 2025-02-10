def solution(input):
    # Mapping of input prefixes to their corresponding coordinates
    coordinates = {
        "18SUJ": "39.239, -77.175",
        "33TWN": "47.364, 15.163",
        "11SJB": "37.376, -121.378"
    }
    
    # Extract the prefix from the input
    prefix = input[:5]
    
    # Return the corresponding coordinates or a default message if not found
    return coordinates.get(prefix, "Coordinates not found")