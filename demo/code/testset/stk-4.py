def solution(input):
    # Use a set to keep track of distinct characters
    distinct_chars = set()
    # Use a list to maintain the order of first appearance
    result = []
    
    for char in input:
        if char not in distinct_chars:
            distinct_chars.add(char)
            result.append(char)
    
    # Join the list into a string to form the output
    output = ''.join(result)
    return output