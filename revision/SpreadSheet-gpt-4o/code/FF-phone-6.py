def solution(input):
    # Split the input string by spaces to separate the country code
    parts = input.split()
    
    # Further split the second part by hyphens to isolate the middle digits
    number_parts = parts[1].split('-')
    
    # The middle three digits are the first part after splitting by hyphens
    middle_digits = number_parts[0]
    
    return middle_digits

# Example usage:
# print(solution("+62 647-787-775"))  # Output: 647
# print(solution("+6 775-969-238"))   # Output: 775
# print(solution("+172 027-507-632")) # Output: 027