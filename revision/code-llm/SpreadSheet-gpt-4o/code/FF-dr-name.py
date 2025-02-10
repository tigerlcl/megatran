def solution(input):
    # Split the input string into words
    words = input.split()
    # The desired output is "Dr." followed by the first word
    output = f"Dr. {words[0]}"
    return output