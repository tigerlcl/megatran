def solution(input):
    # Split the input string by spaces
    parts = input.split()
    
    # Iterate through the parts to find the one that ends with 'ft2'
    for part in parts:
        if part.endswith('ft2'):
            # Extract the number part and return it
            output = part[:-3]
            return output

# Example usage:
# print(solution("Mar 5 Modern studio available $1200 / 1br - 500ft2 - (Downtown Seattle)"))  # Output: 500
# print(solution("Sept 18 Spacious 2-bedroom $1800 / 2br - 850ft2 - (Bellevue Heights)"))  # Output: 850
# print(solution("Jan 29 Luxury penthouse $3500 / 3br - 1500ft2 - (Seattle Waterfront)"))  # Output: 1500