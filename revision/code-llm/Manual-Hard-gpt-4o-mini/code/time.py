def solution(input):
    # Split the input string into hours, minutes, and seconds
    hours, minutes, seconds = map(int, input.split(':'))
    
    # Convert the time into hours as a decimal
    total_hours = hours + minutes / 60 + seconds / 3600
    
    # Format the output to 4 decimal places
    output = f"{total_hours:.4f} hours"
    
    return output