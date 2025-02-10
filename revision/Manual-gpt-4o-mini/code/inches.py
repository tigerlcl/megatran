def solution(input):
    # Extract the number of centimeters from the input string
    cm = int(input.split()[0])
    
    # Convert centimeters to total inches
    total_inches = cm / 2.54
    
    # Calculate feet and remaining inches
    feet = total_inches // 12
    inches = total_inches % 12
    
    # Format the output string
    output = f"{int(feet)} feet and {inches:.4f} inches"
    
    return output