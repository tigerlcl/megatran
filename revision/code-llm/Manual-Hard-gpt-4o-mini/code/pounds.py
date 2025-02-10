def solution(input):
    # Split the input into pounds and ounces
    parts = input.split()
    pounds = float(parts[0].replace('lb', ''))
    ounces = float(parts[1].replace('oz', ''))
    
    # Convert pounds to ounces (1 lb = 16 oz)
    total_ounces = (pounds * 16) + ounces
    
    # Convert ounces to grams (1 oz = 28.3495 g)
    grams = total_ounces * 28.3495
    
    # Round to the nearest whole number and format the output
    output = f"{round(grams)}g"
    
    return output