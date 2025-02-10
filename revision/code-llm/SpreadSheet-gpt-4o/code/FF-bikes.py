def solution(input):
    # Find the first occurrence of a digit in the input string
    for i, char in enumerate(input):
        if char.isdigit():
            # Return the substring from the start to the first digit
            return input[:i]
    # If no digit is found, return the whole input (though not expected in this problem)
    return input