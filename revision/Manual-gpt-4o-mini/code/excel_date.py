def solution(input):
    import datetime
    
    # Convert input string to an integer
    excel_date = int(input)
    
    # Excel date system starts from 1900-01-01, but Excel incorrectly considers 1900 as a leap year
    # So we need to adjust for that by subtracting 1 day for dates after February 28, 1900
    if excel_date > 59:  # 59 corresponds to February 28, 1900
        excel_date -= 1
    
    # Calculate the corresponding date
    base_date = datetime.datetime(1899, 12, 31)  # Correct base date for Excel
    result_date = base_date + datetime.timedelta(days=excel_date)
    
    # Format the output as "YYYY/M/D"
    output = f"{result_date.year}/{result_date.month}/{result_date.day}"
    
    return output