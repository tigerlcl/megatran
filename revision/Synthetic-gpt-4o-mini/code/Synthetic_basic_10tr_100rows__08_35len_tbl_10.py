def solution(input):
    # Step 1: Replace digits with their corresponding letters (0-9 -> a-j)
    digit_to_letter = str.maketrans('0123456789', 'abcdefghij')
    normalized = input.translate(digit_to_letter)
    
    # Step 2: Keep alphanumeric characters, spaces, and specific special characters
    allowed_characters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ()")
    normalized = ''.join(char for char in normalized if char in allowed_characters)
    
    # Step 3: Reverse the string
    normalized = normalized[::-1]
    
    # Step 4: Return the transformed string
    return normalized

# Example usage:
print(solution("zMw7675 7uQ -yDm1j8Qq)j(5"))  # Example output
print(solution("wK41NqeLvh"))  # Example output
print(solution("eo5U*sqZMf0fc 6"))  # Example output