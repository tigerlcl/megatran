def solution(input):
    # Format the input string into the desired phone number format
    output = f"({input[:3]}) {input[3:6]}-{input[6:]}"
    return output