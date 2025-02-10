def solution(input):
    # Parse the input string to convert it into a list of sets
    input_data = eval(input)
    
    # Access the second element of the last set
    output = list(input_data[-1])[-1]
    
    return output