def solution(input):
    # Split the input string into characters
    chars = list(input)
    
    # Reverse the list of characters
    chars.reverse()
    
    # Create a new list to hold the transformed characters
    transformed = []
    
    # Iterate through the reversed characters
    for char in chars:
        # Append each character to the transformed list
        transformed.append(char)
    
    # Join the transformed list into a string
    output = ''.join(transformed)
    
    return output