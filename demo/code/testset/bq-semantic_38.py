import mgrs

def solution(input):
    # Create an instance of the MGRS class
    m = mgrs.MGRS()
    
    try:
        # Convert MGRS to latitude and longitude
        lat, lon = m.toLatLon(input)
        
        # Format the output to 5 decimal places
        output = f"{lat:.5f}, {lon:.5f}"
        
        return output
    except Exception as e:  # Catching a general exception
        return f"Error: {str(e)} - Please provide a valid MGRS string."