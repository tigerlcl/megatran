def solution(input):
    # Check if the input string has enough characters
    if len(input) < 10:
        return ""  # Return an empty string if not enough characters
    
    # Extracting substring of 6 characters starting from position 4
    output = input[4:10]  # This extracts characters from index 4 to index 9 (6 characters)
    return output