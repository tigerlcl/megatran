from datetime import datetime, timedelta

def solution(input):
    # Define the format for parsing the input string
    input_format = "%I:%M %p,%a,%b %d,%Y"
    
    # Parse the input string into a datetime object
    pacific_time = datetime.strptime(input, input_format)
    
    # Convert Pacific Time to Eastern Time (ET is 3 hours ahead of PT)
    eastern_time = pacific_time + timedelta(hours=3)
    
    # Define the format for the output string with correct placement of commas
    output_format = "%I:%M %p,%a,%b,%d,%Y"
    
    # Format the Eastern Time back to string
    output = eastern_time.strftime(output_format).strip()
    
    return output