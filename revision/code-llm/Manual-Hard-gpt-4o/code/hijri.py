from hijri_converter import convert
import datetime

def solution(input):
    # Split the input string
    parts = input.split()
    
    if len(parts) == 3:
        # Case with day, month, and year
        day = int(parts[0])
        month = parts[1]
        year = int(parts[2])
        
        # Convert Hijri date to Gregorian date
        hijri_date = convert.Hijri(year, month, day)
        gregorian_date = hijri_date.to_gregorian()
        
        # Get the day of the week
        day_of_week = gregorian_date.strftime('%A')
        
        # Format the output
        output = f"{day_of_week}, {gregorian_date.strftime('%d %B %Y')} C.E."
    else:
        # Case with only month and year
        month = parts[0]
        year = int(parts[1])
        
        # Convert Hijri date to Gregorian date (using the first day of the month)
        hijri_date = convert.Hijri(year, month, 1)
        gregorian_date = hijri_date.to_gregorian()
        
        # Format the output
        output = f"{gregorian_date.strftime('%B %Y')} C.E."
    
    return output