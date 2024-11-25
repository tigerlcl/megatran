def solution(input):
    # Using a set to store distinct characters
    distinct_characters = set()
    output = ""
    
    # Iterate through each character in the input string
    for char in input:
        # If the character is not already in the set, add it
        if char not in distinct_characters:
            distinct_characters.add(char)
            output += char  # Append to output string
    
    return output