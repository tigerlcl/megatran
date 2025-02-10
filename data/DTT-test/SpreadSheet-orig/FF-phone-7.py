def solution(input):
    # Remove any spaces from the input string
    input = input.replace(" ", "")
    
    # Split the input string by hyphens to isolate the phone number parts
    parts = input.split('-')
    
    # Extract the last part of the phone number which contains the last three digits
    last_part = parts[-1]  # No need to strip as we removed spaces
    
    # Return the last three digits
    return last_part[-3:]

# Example usage:
# print(solution("+62 647-787-775"))  # Output: 775
# print(solution("+6 775-969-238"))   # Output: 238
# print(solution("+106 769-858-438")) # Output: 438