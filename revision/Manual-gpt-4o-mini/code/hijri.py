from hijri_converter import Hijri, Gregorian

def solution(input):
    # Split the input to get the Hijri date components
    parts = input.split()
    
    # Extract the month and year, and handle the day if present
    if len(parts) == 3:
        day = int(parts[0])
        month_name = parts[1]
        year = int(parts[2])
    elif len(parts) == 2:
        day = 1  # Default to the first day of the month
        month_name = parts[0]
        year = int(parts[1])
    else:
        return "Invalid input format"

    # Mapping of Hijri month names to their corresponding month numbers
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

    # Get the month number from the month name
    if month_name in hijri_month_map:
        month = hijri_month_map[month_name]
    else:
        return "Invalid month name"

    # Convert Hijri date to Gregorian date
    hijri_date = Hijri(year, month, day)
    gregorian_date = hijri_date.to_gregorian()

    # Format the output
    output = f"{gregorian_date.day} {gregorian_date.month_name()} {gregorian_date.year} C.E."
    
    # Return the formatted output
    return output