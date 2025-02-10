from hijri_converter import convert

def solution(input):
    # Split the input to extract the Gregorian date components
    parts = input.split()
    
    if len(parts) == 4:
        # Format: "Day, DD Month YYYY C.E."
        day = int(parts[1].replace(',', ''))
        month = parts[2]
        year = int(parts[3])
    elif len(parts) == 3:
        # Format: "Month YYYY C.E."
        day = 1  # Default to the first day of the month
        month = parts[0]
        year = int(parts[1])
    else:
        return "Invalid input format"
    
    # Convert month name to month number
    month_names = {
        "January": 1, "February": 2, "March": 3, "April": 4,
        "May": 5, "June": 6, "July": 7, "August": 8,
        "September": 9, "October": 10, "November": 11, "December": 12
    }
    
    if month not in month_names:
        return "Invalid month name"
    
    month_num = month_names[month]
    
    # Convert Gregorian date to Hijri date
    hijri_date = convert.Gregorian(year, month_num, day).to_hijri()
    
    # Format the Hijri date as "DD Month YYYY"
    hijri_month_names = [
        "Muharram", "Safar", "Rabi' al-awwal", "Rabi' al-thani",
        "Jumada al-awwal", "Jumada al-thani", "Rajab", "Sha'ban",
        "Ramadan", "Shawwal", "Dhu al-Qi'dah", "Dhu al-Hijjah"
    ]
    
    hijri_month = hijri_month_names[hijri_date.month - 1]
    hijri_year = hijri_date.year
    
    if len(parts) == 4:
        hijri_day = hijri_date.day
        output = f"{hijri_day} {hijri_month} {hijri_year}"
    else:
        output = f"{hijri_month} {hijri_year}"
    
    return output