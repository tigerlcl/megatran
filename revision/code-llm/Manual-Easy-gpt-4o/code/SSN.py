def solution(input):
    # Split the input string into three parts
    part1 = input[:3]
    part2 = input[3:6]
    part3 = input[6:]
    
    # Concatenate the parts with dashes
    output = f"{part1}-{part2}-{part3}"
    
    return output