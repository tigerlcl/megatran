def solution(input):
    # Split the input string into first and last names
    names = input.split()
    # Swap the first and last names
    output = f"{names[-1]} {names[0]}"
    return output