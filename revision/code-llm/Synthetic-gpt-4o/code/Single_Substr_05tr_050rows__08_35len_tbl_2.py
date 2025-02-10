def solution(input):
    # Iterate through the input string
    for i in range(len(input) - 1):
        # Check if the current character is a digit and the next character is not a digit
        if input[i].isdigit() and not input[i + 1].isdigit():
            # Return the substring up to and including the next character
            return input[:i + 2]
    # If no such pattern is found, return the entire input
    return input