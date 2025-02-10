def solution(input):
    # Remove numeric displacement designations from motorcycle models
    output = ''.join([char for char in input if not char.isdigit()])
    return output