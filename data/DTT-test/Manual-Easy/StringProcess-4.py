def solution(input):
    # Coding here...
    import string
    output = input.translate(str.maketrans('', '', string.punctuation))
    return output