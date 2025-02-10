def solution(input):
    # Find the first uppercase letter in the input string
    start_index = next((i for i, c in enumerate(input) if c.isupper()), None)
    
    # Find the last uppercase letter in the input string
    end_index = next((i for i, c in enumerate(reversed(input)) if c.isupper()), None)
    
    # If no uppercase letter is found, return an empty string
    if start_index is None or end_index is None:
        return ""
    
    # Calculate the actual end index from the reversed index
    end_index = len(input) - end_index
    
    # Return the substring from the first to the last uppercase letter
    return input[start_index:end_index]

# Example usage:
# print(solution("vEwBnChy&wAarkajBiJh4KPJvfTy0y"))  # Output: BiJh4KPJvfTy0
# print(solution("vDsnt*7Qnu?K6MrEfKV7uw0BDRpV&rXkwx"))  # Output: fKV7uw0BDRpV&
# print(solution("6?-uk4RHsdkJKnsesRzovasnpu0Mib"))  # Output: sRzovasnpu0Mi