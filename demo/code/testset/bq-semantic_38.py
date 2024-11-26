def solution(input):
    from mgrs import MGRS

    # Initialize the MGRS converter
    mgrs_converter = MGRS()
    
    try:
        # Convert the MGRS coordinate to latitude and longitude
        lat, lon = mgrs_converter.toLatLon(input)
        
        # Format the output to match the required precision
        output = f"{lat:.5f}, {lon:.5f}"
    except Exception as e:
        # Handle any exceptions that occur during conversion
        output = f"Invalid MGRS input: {e}"
    
    return output