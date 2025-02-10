def solution(input):
    import re
    match = re.search(r'(\d+)ft2', input)
    if match:
        return match.group(1)
    return ""

# Example usage:
# print(solution("Mar 5 Modern studio available $1200 / 1br - 500ft2 - (Downtown Seattle)"))  # Output: 500
# print(solution("Sept 18 Spacious 2-bedroom $1800 / 2br - 850ft2 - (Bellevue Heights)"))  # Output: 850
# print(solution("Jan 29 Luxury penthouse $3500 / 3br - 1500ft2 - (Seattle Waterfront)"))  # Output: 1500