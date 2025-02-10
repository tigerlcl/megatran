def solution(input):
    # Split the input string into pounds and ounces
    parts = input.split()
    pounds = float(parts[0].replace('lb', ''))
    ounces = float(parts[1].replace('oz', ''))
    
    # Convert pounds and ounces to grams
    grams = (pounds * 453.592) + (ounces * 28.3495)
    
    # Round to the nearest integer and format the output
    output = f"{int(round(grams))}g"
    return output