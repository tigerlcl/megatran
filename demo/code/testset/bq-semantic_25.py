from hijridate import Hijri, Gregorian

def solution(input):
    # Parse the input Hijri date
    hijri_day, hijri_month, hijri_year = input.split()
    
    # Convert Hijri month name to number
    hijri_month_map = {
        'Muharram': 1,
        'Safar': 2,
        'Rabi\' al-Awwal': 3,
        'Rabi\' al-Thani': 4,
        'Jumada al-Awwal': 5,
        'Jumada al-Thani': 6,
        'Rajab': 7,
        'Sha\'ban': 8,
        'Ramadan': 9,
        'Shawwal': 10,
        'Dhu al-Qi\'dah': 11,
        'Dhu al-Hijjah': 12
    }
    
    # Validate the Hijri year
    hijri_year = int(hijri_year)
    if hijri_year < 1343 or hijri_year > 1500:
        raise ValueError(f"Hijri year must be between 1343 and 1500, got '{hijri_year}'")
    
    # Convert the Hijri date to Gregorian
    hijri_date = Hijri(hijri_year, hijri_month_map[hijri_month], int(hijri_day))
    gregorian_date = hijri_date.to_gregorian()
    
    # Format the output
    output = f"{gregorian_date.day} {gregorian_date.month_name()} {gregorian_date.year} C.E"
    
    # Get the day of the week
    day_of_week = gregorian_date.strftime('%A')
    
    # Combine day of the week with the output
    final_output = f"{day_of_week} {output}"
    
    return final_output