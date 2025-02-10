def solution(input):
    # Convert the input string to a list of sets
    data = eval(input)
    
    # Access the second element of the last set
    output = list(data[-1])[-1]
    
    return output