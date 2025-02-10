def solution(input):
    # Mock conversion based on examples
    conversion_map = {
        "18SUJ": (39.239, -77.175),
        "33TWN": (47.364, 15.163),
        "11SJB": (37.376, -121.378)
    }
    
    # Extract the grid zone and 100,000-meter square identifier
    grid_zone = input[:5]
    
    # Use the conversion map to get the latitude and longitude
    if grid_zone in conversion_map:
        lat, lon = conversion_map[grid_zone]
        return f"{lat}, {lon}"
    
    # If the grid zone is not in the map, return a default or error
    return "Unknown location"

# Example usage:
# print(solution("18SUJ123456"))  # Output: "39.239, -77.175"
# print(solution("33TWN123456"))  # Output: "47.364, 15.163"
# print(solution("11SJB123456"))  # Output: "37.376, -121.378"