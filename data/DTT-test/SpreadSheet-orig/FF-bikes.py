def solution(input):
    # Remove numeric displacement designations from motorcycle model names
    output = ''.join(filter(lambda x: not x.isdigit(), input))
    return output