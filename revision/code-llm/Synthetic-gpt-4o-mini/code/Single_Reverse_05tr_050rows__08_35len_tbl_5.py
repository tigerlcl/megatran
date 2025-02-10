def solution(input):
    # Split the input into words
    words = input.split()
    
    # Reverse each word and store them in a list
    reversed_words = [word[::-1] for word in words]
    
    # Reverse the list of reversed words
    reversed_words.reverse()
    
    # Join the reversed words into a single string
    output = ' '.join(reversed_words)
    
    return output