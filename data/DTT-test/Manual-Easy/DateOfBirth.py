def solution(input):
    # Extract year, month, and day from the input string
    year = input[:4]
    month = input[4:6]
    day = input[6:]
    
    # Format the date as MM-DD-YYYY
    output = f"{month}-{day}-{year}"
    
    return output