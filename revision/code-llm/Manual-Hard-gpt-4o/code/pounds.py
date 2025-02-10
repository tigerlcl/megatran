def solution(input):
    # Split the input into pounds and ounces
    parts = input.split()
    pounds = float(parts[0][:-2])
    ounces = float(parts[1][:-2])
    
    # Convert pounds to grams (1 pound = 453.59237 grams)
    grams_from_pounds = pounds * 453.59237
    
    # Convert ounces to grams (1 ounce = 28.3495231 grams)
    grams_from_ounces = ounces * 28.3495231
    
    # Total grams
    total_grams = grams_from_pounds + grams_from_ounces
    
    # Round the result to the nearest whole number
    total_grams = round(total_grams)
    
    # Format the output
    output = f"{total_grams}g"
    
    return output