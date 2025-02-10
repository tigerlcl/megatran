def solution(input):
    # Extract substring starting from the fifth character and retain a maximum of 35 characters
    substring = input[4:]  # Start from index 4 to the end
    output = substring[-35:]  # Get the last 35 characters of the substring
    return output