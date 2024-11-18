from hijridate import Hijri, Gregorian

def solution(input):
    # Split the input string to extract day, month, and year
    hijri_date_parts = input.split()
    day = int(hijri_date_parts[0])
    month = hijri_date_parts[1]
    year = int(hijri_date_parts[2])
    
    # Map Hijri month names to numbers
    hijri_month_map = {
        "Muharram": 1,
        "Safar": 2,
        "Rabi' al-Awwal": 3,
        "Rabi' al-Thani": 4,
        "Jumada al-Awwal": 5,
        "Jumada al-Thani": 6,
        "Rajab": 7,
        "Sha'ban": 8,
        "Ramadan": 9,
        "Shawwal": 10,
        "Dhu al-Qi'dah": 11,
        "Dhu al-Hijjah": 12
    }
    
    # Get the month number from the map
    month_number = hijri_month_map[month]
    
    # Create a Hijri date object
    hijri_date = Hijri(year, month_number, day)
    
    # Convert to Gregorian
    gregorian_date = hijri_date.to_gregorian()
    
    # Format the output string
    output = f"{gregorian_date.day} {gregorian_date.month_name} {gregorian_date.year} C.E"
    
    # Get the day of the week
    day_of_week = gregorian_date.day_of_week()
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Combine day of the week with the output
    output = f"{days[day_of_week]} {output}"
    
    return output