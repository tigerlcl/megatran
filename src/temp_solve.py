def solution(input):
    # Convert the input string to a float
    kg = float(input)
    
    # Conversion factor from kilograms to pounds
    conversion_factor = 2.20462
    
    # Convert kilograms to pounds
    pounds = kg * conversion_factor
    
    # Round the result to one digit after the decimal
    rounded_pounds = round(pounds, 1)
    
    return rounded_pounds