def solution(input):
    # Split the input text into words
    words = input.split()
    
    # Extract uppercase words
    output = [word for word in words if word.isupper()]
    
    return output