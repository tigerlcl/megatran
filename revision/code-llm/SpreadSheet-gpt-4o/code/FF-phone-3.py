def solution(input):
    # Split the input string into three parts using the '-' delimiter
    parts = input.split('-')
    
    # Format the output string using the desired pattern
    output = f"({parts[0]}) {parts[1]}-{parts[2]}"
    
    return output