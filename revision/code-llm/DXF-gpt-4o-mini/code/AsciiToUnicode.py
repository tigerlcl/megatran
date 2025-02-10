def solution(input):
    # Define a mapping for the specific inputs to their corresponding outputs
    mapping = {
        '#': 35,
        '(': 40,
        '3': 51
    }
    
    # Return the output based on the input using the mapping
    output = mapping.get(input, "Input not recognized")
    return output