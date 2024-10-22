def solution(input):
    # Split the input string by '/'
    year, month, day = input.split('/')
    
    # Format the month, day, and year with leading zeros
    output = f"{int(month):02}/{int(day):02}/{year}"
    
    return output