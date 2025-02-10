def solution(input):
    # Remove the '+' sign and any non-numeric characters
    cleaned_number = ''.join(filter(str.isdigit, input))
    
    # Determine the size of the first group
    first_group_size = len(cleaned_number) % 3 or 3
    
    # Insert dots at the appropriate positions
    formatted_number = '.'.join(
        [cleaned_number[:first_group_size]] + 
        [cleaned_number[i:i+3] for i in range(first_group_size, len(cleaned_number), 3)]
    )
    
    return formatted_number