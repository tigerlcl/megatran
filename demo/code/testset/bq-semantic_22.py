from datetime import datetime, timedelta

def solution(input):
    # Define the format of the input date string
    date_format = "%I:%M %p,%a,%b %d,%Y"
    
    # Parse the input string into a datetime object
    pacific_time = datetime.strptime(input, date_format)
    
    # Convert Pacific Time to Eastern Time (PT is 3 hours behind ET)
    eastern_time = pacific_time + timedelta(hours=3)
    
    # Format the output string
    output = eastern_time.strftime(date_format)
    
    return output