from datetime import datetime
import pytz

def solution(input):
    # Define the formats for parsing the input
    formats = [
        "%A %d de %B de %Y",  # e.g., Martes 21 de Octubre de 2014
        "%A, %d-%b-%y %H:%M:%S %Z",  # e.g., Monday, 02-Jan-06 15:04:05 MST
        "%Y-%m-%d %H:%M:%S.%f"  # e.g., 2012-08-03 18:31:59.257000000
    ]
    
    # Attempt to parse the input with each format
    for fmt in formats:
        try:
            # Parse the date string
            dt = datetime.strptime(input, fmt)
            # If the format is the second one, we need to set the timezone
            if fmt == formats[1]:
                dt = dt.replace(tzinfo=pytz.timezone('MST'))
            # Convert to UTC
            dt = dt.astimezone(pytz.utc)
            # Format the output
            output = dt.isoformat()
            return output
        except ValueError:
            continue
    
    # If no format matched, raise an error
    raise ValueError("Input date format is not recognized.")