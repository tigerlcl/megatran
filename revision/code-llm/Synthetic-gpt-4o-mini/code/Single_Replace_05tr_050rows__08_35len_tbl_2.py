def solution(input):
    # Split the input string into words
    words = input.split()
    
    # Process each word to replace the last character with 'r' if it's not already 'r'
    transformed_words = []
    for word in words:
        if word and word[-1] != 'r':
            transformed_word = word[:-1] + 'r'
        else:
            transformed_word = word
        transformed_words.append(transformed_word)
    
    # Join the transformed words back into a single string
    output = ' '.join(transformed_words)
    return output