def solution(input):
    # Split the input string by spaces and hyphens to isolate the number parts
    parts = input.split()
    # The last part will be in the format 'xxx-xxx-xxx'
    last_part = parts[-1]
    # Split the last part by hyphen and get the second last element
    last_three_digits = last_part.split('-')[-2]
    return last_three_digits