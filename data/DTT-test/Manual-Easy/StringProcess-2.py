def solution(input):
    # Split the input string by semicolon to get the arrays
    arrays = input.split(';')
    # Split the first array by comma to get the elements
    first_array_elements = arrays[1].split(',')
    # Extract the first element from the first array, strip any leading/trailing whitespace
    output = first_array_elements[0].strip()
    return output