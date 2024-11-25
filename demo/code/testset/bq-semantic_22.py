from datetime import datetime, timedelta

def solution(input):
    # Define the format of the input string
    input_format = "%I:%M %p,%a,%b %d,%Y"
    
    # Parse the input string into a datetime object
    pacific_time = datetime.strptime(input, input_format)
    
    # Convert Pacific Time to Eastern Time (PT is 3 hours behind ET)
    eastern_time = pacific_time + timedelta(hours=3)
    
    # Format the output string without leading zeros for the hour
    output_format = "%-I:%M %p,%a,%b %d %Y"
    output = eastern_time.strftime(output_format)
    
    return output