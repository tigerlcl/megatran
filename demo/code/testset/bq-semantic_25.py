from hijri_converter import Hijri, Gregorian

def solution(input):
    # Split the input string into components
    hijri_date_parts = input.split()
    hijri_day = int(hijri_date_parts[0])
    hijri_month = hijri_date_parts[1]
    hijri_year = int(hijri_date_parts[2])
    
    # Map Hijri month names to numbers
    hijri_month_map = {
        'Muharram': 1,
        'Safar': 2,
        'Rabi al-Awwal': 3,
        'Rabi al-Thani': 4,
        'Jumada al-Awwal': 5,
        'Jumada al-Thani': 6,
        'Rajab': 7,
        'Sha\'ban': 8,
        'Ramadan': 9,
        'Shawwal': 10,
        'Dhu al-Qi\'dah': 11,
        'Dhu al-Hijjah': 12
    }
    
    # Get the month number from the map
    hijri_month_number = hijri_month_map[hijri_month]
    
    # Create a Hijri date object
    hijri_date = Hijri(hijri_year, hijri_month_number, hijri_day)
    
    # Convert to Gregorian date
    gregorian_date = hijri_date.to_gregorian()
    
    # Format the output
    output = f"{gregorian_date.day} {gregorian_date.month} {gregorian_date.year} C.E"
    
    # Get the day of the week
    day_of_week = gregorian_date.strftime("%A")
    
    # Combine day of the week with the output
    final_output = f"{day_of_week} {output}"
    
    return final_output