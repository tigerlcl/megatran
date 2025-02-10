def solution(input):
    # Split the input into parts
    parts = input.split()
    
    # Define the prefix
    prefix = "9LAxH"
    
    # Initialize an empty list to hold modified parts
    modified_parts = []
    
    # Process each part
    for index, part in enumerate(parts):
        if index == 0:
            modified_parts.append(prefix + " " + part)  # Keep original casing
        else:
            # Modify the part for obfuscation
            modified_part = part[::-1]  # Reverse the part
            modified_parts.append(modified_part + part.upper())  # Append uppercased part
    
    # Join the modified parts into a single output string
    output = " ".join(modified_parts)
    
    return output