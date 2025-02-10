def solution(input):
    # Find the last occurrence of 'M' in the input string
    last_m_index = input.rfind('M')
    
    # If 'M' is found, extract the substring starting from the character after 'M'
    if last_m_index != -1:
        output = input[last_m_index + 1:last_m_index + 1 + 15]  # Extract next 15 characters
    else:
        output = ""  # If 'M' is not found, return an empty string
    
    return output