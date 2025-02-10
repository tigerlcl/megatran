def solution(input):
    # Split the input into characters
    chars = list(input)
    # Create a list to hold the reversed characters
    reversed_chars = [''] * len(chars)
    
    # Pointers for the start and end of the input
    left, right = 0, len(chars) - 1
    
    while left <= right:
        # Move left pointer to the next alphanumeric character
        while left <= right and not chars[left].isalnum():
            reversed_chars[left] = chars[left]
            left += 1
        # Move right pointer to the previous alphanumeric character
        while left <= right and not chars[right].isalnum():
            reversed_chars[right] = chars[right]
            right -= 1
        
        # If both pointers are still valid, swap the characters
        if left <= right:
            reversed_chars[left] = chars[right]  # Correctly assign chars[right] to reversed_chars[left]
            reversed_chars[right] = chars[left]  # Correctly assign chars[left] to reversed_chars[right]
            left += 1
            right -= 1
    
    # Join the list into a string and return
    return ''.join(reversed_chars)