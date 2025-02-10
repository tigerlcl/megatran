def solution(input):
    # Split the input string into first and last name
    names = input.split()
    # Rearrange the names to last name first
    output = f"{names[1]} {names[0]}"
    return output