from hijri_converter import convert

def solution(input):
    # Split the input to extract the date components
    parts = input.split(",")[1].strip().split(" ")
    day = int(parts[0])
    month = parts[1]
    year = int(parts[2].replace("C.E.", "").strip())
    
    # Convert the Gregorian date to Hijri date
    hijri_date = convert.Gregorian(year, month_to_number(month), day).to_hijri()
    
    # Format the output as required
    output = f"{hijri_date.month_name} {hijri_date.year}"
    return output

def month_to_number(month):
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }
    return months[month]