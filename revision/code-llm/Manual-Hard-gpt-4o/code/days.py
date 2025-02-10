from datetime import datetime

def solution(input):
    # Define the start date
    start_date = datetime(1900, 1, 1)
    
    # Parse the input date
    input_date = datetime.strptime(input, "%Y/%m/%d")
    
    # Calculate the difference in days
    days_difference = (input_date - start_date).days
    
    return str(days_difference)