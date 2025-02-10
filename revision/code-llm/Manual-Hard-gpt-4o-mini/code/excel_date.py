def solution(input):
    # Convert the input string to an integer
    num = int(input)
    
    # Calculate the year, month, and day based on the input number
    if num < 10000:
        year = 1900 + (num // 100)
        month = (num % 100) // 10
        day = (num % 10) + 10
    else:
        year = 2000 + (num // 10000)
        month = (num // 100) % 100
        day = num % 100
    
    # Format the output as a string
    output = f"{year}/{month}/{day}"
    return output