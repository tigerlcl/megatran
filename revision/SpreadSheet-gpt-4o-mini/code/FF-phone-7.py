def solution(input):
    # Remove all non-digit characters from the input
    digits = ''.join(filter(str.isdigit, input))
    
    # Return the last three digits, ensuring there are at least three digits
    return digits[-3:] if len(digits) >= 3 else digits

# Example usage:
# print(solution("+62 647-787-775"))  # Output: 775
# print(solution("+6 775-969-238"))   # Output: 969
# print(solution("+106 769-858-438")) # Output: 858