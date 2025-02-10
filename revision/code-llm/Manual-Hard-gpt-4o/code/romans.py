def solution(input):
    # Define a dictionary to map Roman numerals to their integer values
    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # Initialize the total to 0
    total = 0
    # Iterate over the input string
    for i in range(len(input)):
        # If the current numeral is less than the next numeral, subtract it
        if i + 1 < len(input) and roman_to_int[input[i]] < roman_to_int[input[i + 1]]:
            total -= roman_to_int[input[i]]
        else:
            # Otherwise, add it
            total += roman_to_int[input[i]]
    
    # Return the total as a string
    return str(total)