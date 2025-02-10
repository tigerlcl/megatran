def solution(input):
    # Reverse the input string
    reversed_input = input[::-1]
    
    # Split the reversed string into words
    words = reversed_input.split()
    
    # Reverse each word and join them back with spaces
    transformed_words = [''.join(reversed(word)) for word in words]
    
    # Join the transformed words back into a single string
    output = ' '.join(transformed_words)
    
    return output