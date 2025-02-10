def solution(input):
    # Split the input string by spaces
    parts = input.split()
    # Iterate through the parts to find the price
    for part in parts:
        if part.startswith('$'):
            # Remove the dollar sign and return the price
            return part[1:]
    return ""

# Example usage:
# print(solution("Mar 5 Modern studio available $1200 / 1br - 500ft2 - (Downtown Seattle)"))  # Output: 1200
# print(solution("Sept 18 Spacious 2-bedroom $1800 / 2br - 850ft2 - (Bellevue Heights)"))    # Output: 1800
# print(solution("Jan 29 Luxury penthouse $3500 / 3br - 1500ft2 - (Seattle Waterfront)"))    # Output: 3500