def solution(input):
    # Remove the first and last character if they are quotation marks
    if input.startswith('"') and input.endswith('"'):
        return input[1:-1]
    return input