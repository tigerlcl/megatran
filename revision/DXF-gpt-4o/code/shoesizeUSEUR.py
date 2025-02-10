def solution(input):
    # Convert the input string to a float
    us_size = float(input)
    
    # Conversion formula from US to EU shoe size
    eu_size = us_size + 32
    
    # Format the output to one decimal place
    output = f"{eu_size:.1f}"
    
    return output