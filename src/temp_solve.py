def solution(input):
    # Convert the input string to a float
    kgs = float(input)
    
    # Conversion factor from kilograms to pounds
    conversion_factor = 2.20462
    
    # Convert kilograms to pounds
    pounds = kgs * conversion_factor
    
    # Round to one digit after the decimal
    rounded_pounds = round(pounds, 1)
    
    return rounded_pounds