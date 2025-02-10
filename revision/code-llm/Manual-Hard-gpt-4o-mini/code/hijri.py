def solution(input):
    from hijri_converter import Hijri, Gregorian

    # Split the input to get the month and year
    parts = input.split()
    
    # Determine if the input has a day or just a month and year
    if len(parts) == 3:
        day = int(parts[0])
        month = parts[1]
        year = int(parts[2])
        
        # Convert Hijri date to Gregorian
        hijri_date = Hijri(year, month, day)
        gregorian_date = hijri_date.to_gregorian()
        
        # Format the output
        output = f"{gregorian_date.day} {gregorian_date.month_name} {gregorian_date.year} C.E."
    elif len(parts) == 2:
        month = parts[0]
        year = int(parts[1])
        
        # Convert Hijri month and year to Gregorian
        hijri_date = Hijri(year, month, 1)  # Use the first day of the month
        gregorian_date = hijri_date.to_gregorian()
        
        # Format the output
        output = f"{gregorian_date.month_name} {gregorian_date.year} C.E."
    
    return output