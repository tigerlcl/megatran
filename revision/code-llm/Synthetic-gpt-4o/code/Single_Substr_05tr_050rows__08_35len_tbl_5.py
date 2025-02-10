def solution(input):
    # Find the position of the first uppercase letter in the input string
    for i, char in enumerate(input):
        if char.isupper():
            # Return the substring starting from the first uppercase letter
            return input[i:]
    # If no uppercase letter is found, return an empty string
    return ""