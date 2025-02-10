from datetime import datetime

def solution(input):
    # Convert the input string to a date object
    date_object = datetime.strptime(input, '%Y/%m/%d')
    # Calculate the number of days since the epoch (January 1, 1970)
    epoch = datetime(1970, 1, 1)
    days_since_epoch = (date_object - epoch).days
    # Return the result as a string
    return str(days_since_epoch)