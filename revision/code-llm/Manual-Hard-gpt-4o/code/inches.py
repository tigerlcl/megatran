def solution(input):
    # Extract the numeric value from the input string
    cm = float(input.split()[0])
    
    # Convert cm to inches (1 cm = 0.393701 inches)
    total_inches = cm * 0.393701
    
    # Calculate feet and remaining inches
    feet = int(total_inches // 12)
    inches = total_inches % 12
    
    # Format the output string
    output = f"{feet} feet and {inches:.4f} inches"
    
    return output