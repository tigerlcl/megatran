def solution(input):
    # Remove the 'U+' prefix and convert the remaining hex string to an integer
    unicode_value = int(input[2:], 16)
    # Convert the integer to a zero-padded string of length 3
    ascii_code = f"{unicode_value:03}"
    return ascii_code