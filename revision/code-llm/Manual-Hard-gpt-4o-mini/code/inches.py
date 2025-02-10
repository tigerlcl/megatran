def solution(input):
    # Extract the number from the input string
    cm = int(input.split()[0])
    
    # Conversion constants
    cm_per_inch = 2.54
    inches_per_foot = 12
    
    # Convert cm to total inches
    total_inches = cm / cm_per_inch
    
    # Calculate feet and remaining inches
    feet = int(total_inches // inches_per_foot)
    inches = total_inches % inches_per_foot
    
    # Format the output
    output = f"{feet} feet and {inches:.4f} inches"
    return output