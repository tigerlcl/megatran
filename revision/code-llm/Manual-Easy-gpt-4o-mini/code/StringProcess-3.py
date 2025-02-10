def solution(input):
    # Convert the input string to a list of sets
    input_data = eval(input)
    
    # Extract the first element from the second set
    output = list(input_data[1])[0]
    
    return output