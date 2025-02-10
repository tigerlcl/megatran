def solution(input):
    # Split the input string into words
    words = input.split()
    
    # Initialize an empty list to hold the transformed words
    transformed_words = []
    
    # Iterate through each word
    for word in words:
        # If the word contains a closing parenthesis followed by a character,
        # we need to split it into two parts
        if ')' in word:
            # Find the index of the closing parenthesis
            index = word.index(')')
            # Split the word into two parts: before and after the parenthesis
            before = word[:index + 1]  # Include the closing parenthesis
            after = word[index + 1:]    # The rest of the word
            # Append the transformed parts to the list
            transformed_words.append(before)
            transformed_words.append(after)
        else:
            # If there's no closing parenthesis, just append the word as is
            transformed_words.append(word)
    
    # Join the transformed words back into a single string
    output = ' '.join(transformed_words)
    return output