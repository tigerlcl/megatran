def solution(input):
    from datetime import datetime
    
    # Parse the input date string into a datetime object
    date = datetime.strptime(input, '%Y/%m/%d')
    
    # Calculate the number of days since the epoch (January 1, 1900)
    epoch = datetime(1900, 1, 1)
    delta = date - epoch
    
    # Return the number of days as an integer
    output = str(delta.days)
    return output