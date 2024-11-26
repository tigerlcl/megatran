from datetime import datetime, timedelta

def solution(input):
    try:
        # Parse the input string
        time_str, day, month, date, year = input.split(',')
    except ValueError:
        raise ValueError("Input string must be in the format: 'HH:MM AM/PM,Day,Month,Date,Year'")

    # Create a datetime object from the input string
    time_obj = datetime.strptime(f"{time_str} {day} {month} {date} {year}", "%I:%M %p %a %b %d %Y")
    
    # Convert from Pacific Time to Eastern Time by adding 3 hours
    eastern_time_obj = time_obj + timedelta(hours=3)
    
    # Format the output string
    output_time_str = eastern_time_obj.strftime("%I:%M %p")
    output_day = eastern_time_obj.strftime("%a")
    output_month = eastern_time_obj.strftime("%b")
    output_date = eastern_time_obj.strftime("%d")
    output_year = eastern_time_obj.strftime("%Y")
    
    # Construct the output string
    output = f"{output_time_str},{output_day},{output_month},{output_date},{output_year}"
    
    return output