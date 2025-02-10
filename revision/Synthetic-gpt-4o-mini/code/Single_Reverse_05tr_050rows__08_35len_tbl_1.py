def solution(input):
    # Extract alphanumeric characters
    alphanumeric_chars = [char for char in input if char.isalnum()]
    
    # Reverse the list of alphanumeric characters
    alphanumeric_chars.reverse()
    
    # Iterator for the reversed alphanumeric characters
    it = iter(alphanumeric_chars)
    
    # Build the output string, replacing only alphanumeric characters
    output = ''.join(next(it) if char.isalnum() else char for char in input)
    
    return output