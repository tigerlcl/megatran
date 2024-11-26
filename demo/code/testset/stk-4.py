def solution(input):
    # Using a set to store distinct characters
    distinct_chars = set()
    # Using a list to maintain the order of first appearance
    result = []
    
    for char in input:
        if char not in distinct_chars:
            distinct_chars.add(char)
            result.append(char)
    
    # Joining the list to form the output string
    return ''.join(result)