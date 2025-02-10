def solution(input):
    # Convert the input to an integer
    number = int(input)
    
    # Determine the year
    if number < 36525:
        year = 1900 + (number // 365)
    else:
        year = 2000 + ((number - 36525) // 365)
    
    # Calculate the remaining days after determining the year
    if number < 36525:
        days_remaining = number % 365
    else:
        days_remaining = (number - 36525) % 365
    
    # Determine the month and day
    # Days in each month from January to December
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Adjust for leap years
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29
    
    month = 1
    for days in days_in_month:
        if days_remaining < days:
            break
        days_remaining -= days
        month += 1
    
    # The remaining days are the day of the month
    day = days_remaining + 1
    
    # Format the output as a string
    output = f"{year}/{month}/{day}"
    return output