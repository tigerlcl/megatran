def solution(input):
    last_star_index = input.rfind('*')  # Find the last occurrence of '*'
    if last_star_index == -1:
        return input  # Return the input unchanged if '*' is not found
    output = input[:last_star_index] + 'Z' + input[last_star_index + 1:]  # Replace last '*' with 'Z'
    return output