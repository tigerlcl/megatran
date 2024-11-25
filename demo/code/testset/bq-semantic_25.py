from hijri_converter import Hijri, Gregorian

def solution(input):
    # Split the input string to extract day, month, and year
    parts = input.split()
    day = int(parts[0])
    month = parts[1]
    year = int(parts[2])
    
    # Mapping Hijri month names to numbers
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
    
    # Convert Hijri month name to number
    hijri_month = hijri_month_map[month]
    
    # Create a Hijri date object
    hijri_date = Hijri(year, hijri_month, day)
    
    # Convert to Gregorian date
    gregorian_date = hijri_date.to_gregorian()
    
    # Format the output
    output = gregorian_date.isoformat()
    day_of_week = gregorian_date.strftime("%A")
    formatted_output = f"{day_of_week} {gregorian_date.day} {gregorian_date.strftime('%B')} {gregorian_date.year} C.E"
    
    return formatted_output