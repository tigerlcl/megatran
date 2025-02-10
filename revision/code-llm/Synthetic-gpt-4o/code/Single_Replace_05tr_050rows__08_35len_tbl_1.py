def solution(input):
    # Split the input string into parts
    parts = input.split()
    
    # Initialize an empty list to store transformed parts
    transformed_parts = []
    
    # Iterate over each part
    for part in parts:
        # Check if the part contains a digit followed by a non-digit
        for i in range(len(part) - 1):
            if part[i].isdigit() and not part[i+1].isdigit():
                # Split the part at the position and append both parts to the list
                transformed_parts.append(part[:i+1])
                transformed_parts.append(part[i+1:])
                break
        else:
            # If no split is needed, append the part as is
            transformed_parts.append(part)
    
    # Join the transformed parts with spaces and return
    return ' '.join(transformed_parts)