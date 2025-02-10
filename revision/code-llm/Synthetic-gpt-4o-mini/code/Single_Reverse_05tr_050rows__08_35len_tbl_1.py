def solution(input):
    # Split the input into characters and reverse the list
    reversed_chars = list(input)[::-1]
    
    # Join the reversed characters back into a string
    output = ''.join(reversed_chars)
    
    return output