def solution(input):
    # Split the input string by spaces
    parts = input.split()
    
    # Find the index of the part that contains 'ft2'
    for i in range(len(parts)):
        if 'ft2' in parts[i]:
            # Extract the number before 'ft2' and return it
            return parts[i-1]
    
    return None  # In case no ft2 is found, though it should always be present based on the examples