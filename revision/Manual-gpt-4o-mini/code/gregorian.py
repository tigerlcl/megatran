from hijri_converter import convert

def solution(input):
    # Parse the input date
    if ',' in input:
        # Full date format
        date_str = input.split(',')[1].strip()
    else:
        # Month and year format
        date_str = input.strip()

    # Handle different formats
    if len(date_str.split()) == 3:  # Full date
        day, month, year = date_str.split()
        month = month.capitalize()
        month_number = {
            'January': 1, 'February': 2, 'March': 3, 'April': 4,
            'May': 5, 'June': 6, 'July': 7, 'August': 8,
            'September': 9, 'October': 10, 'November': 11, 'December': 12
        }[month]
        gregorian_date = (int(year), month_number, int(day))
    else:  # Month and year only
        month, year = date_str.split()
        month = month.capitalize()
        month_number = {
            'January': 1, 'February': 2, 'March': 3, 'April': 4,
            'May': 5, 'June': 6, 'July': 7, 'August': 8,
            'September': 9, 'October': 10, 'November': 11, 'December': 12
        }[month]
        gregorian_date = (int(year), month_number, 1)  # Use the first day of the month

    # Convert Gregorian date to Hijri date
    hijri_date = convert.Gregorian(*gregorian_date).to_hijri()
    
    # Format the output
    hijri_months = [
        "Muharram", "Safar", "Rabi' al-Awwal", "Rabi' al-Thani",
        "Jumada al-Awwal", "Jumada al-Thani", "Rajab", "Sha'ban",
        "Ramadan", "Shawwal", "Dhu al-Qi'dah", "Dhu al-Hijjah"
    ]
    
    output = f"{hijri_date.day} {hijri_months[hijri_date.month - 1]} {hijri_date.year}"
    return output