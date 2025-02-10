def solution(input):
    # Split the input time into hours, minutes, and seconds
    hours, minutes, seconds = map(int, input.split(':'))
    
    # Convert the time to decimal format
    decimal_hours = hours + minutes / 60 + seconds / 3600
    
    # Format the output to four decimal places
    output = f"{decimal_hours:.4f} hours"
    
    return output