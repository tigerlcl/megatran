def solution(input):
    # Convert the input string to a float
    kgs = float(input)
    # Convert kilograms to pounds
    pounds = kgs * 2.20462
    # Round the result to one digit after the decimal
    rounded_pounds = round(pounds, 1)
    return rounded_pounds