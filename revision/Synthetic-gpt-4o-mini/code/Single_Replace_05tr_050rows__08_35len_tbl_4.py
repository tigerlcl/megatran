def solution(input):
    # Define the character to be replaced
    char_to_replace = None  # This will be set based on the first character found
    
    # Iterate through the input to find the first character that can be replaced
    for char in input:
        if char.isalpha():  # Check if the character is an alphabet
            char_to_replace = char
            break
    
    if char_to_replace is not None:
        # Find the first occurrence of the character
        index = input.find(char_to_replace)
        # Replace the first occurrence with the character repeated twice
        output = input[:index] + char_to_replace * 2 + input[index + 1:]
    else:
        # If no character is found, return the original input
        output = input
        
    return output