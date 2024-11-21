from datetime import datetime, timedelta

def solution(input):
    # Parse the input string into a datetime object
    dt = datetime.strptime(input, "%I:%M %p,%a,%b %d,%Y")
    
    # Calculate the time difference between PT and ET (ET is 3 hours ahead of PT)
    time_difference = timedelta(hours=3)
    
    # Convert the time from PT to ET by adding the time difference
    et_time = dt + time_difference
    
    # Format the output string without leading zeros for hour and day
    output = et_time.strftime("%-I:%M %p,%a,%b %-d,%Y")
    
    return output