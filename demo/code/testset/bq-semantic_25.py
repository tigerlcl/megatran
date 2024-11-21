from hijri_converter import convert

def solution(input):
    # Mapping of Hijri month names to their numbers
    hijri_months = {
        "Muharram": 1,
        "Safar": 2,
        "Rabi' al-awwal": 3,
        "Rabi' al-thani": 4,
        "Jumada al-awwal": 5,
        "Jumada al-thani": 6,
        "Rajab": 7,
        "Sha'ban": 8,
        "Ramadan": 9,
        "Shawwal": 10,
        "Dhu al-Qi'dah": 11,
        "Dhu al-Hijjah": 12
    }
    
    # Parse the input
    parts = input.split()
    day = int(parts[0])
    month_name = parts[1]
    year = int(parts[2])
    
    # Get the month number
    month = hijri_months[month_name]
    
    # Convert Hijri to Gregorian
    gregorian_date = convert.Hijri(year, month, day).to_gregorian()
    
    # Get the day of the week
    weekday = gregorian_date.strftime('%A')
    
    # Format the output
    output = f"{weekday} {gregorian_date.day} {gregorian_date.strftime('%B')} {gregorian_date.year} C.E"
    
    return output

# Example usage:
# print(solution("11 Shawwal 1430"))  # Output: Wednesday 30 September 2009 C.E
# print(solution("5 Muharram 1300"))  # Output: Thursday 16 November 1882 C.E
# print(solution("19 Rajab 1460"))    # Output: Friday 20 August 2038 C.E