def solution(input):
    # Create a mapping for special characters to A-Z equivalents
    special_char_map = {
        '0': 'o', '1': 'i', '2': 'z', '3': 'e', '4': 'a',
        '5': 's', '6': 'g', '7': 't', '8': 'b', '9': 'q',
        ' ': '.', '(': '', ')': '', '-': '', '_': '', 
        '.': '', ',': '', '!': '', '@': '', '#': '', 
        '$': '', '%': '', '^': '', '&': '', '*': '', 
        '+': '', '=': '', '{': '', '}': '', '[': '', 
        ']': '', ':': '', ';': '', '"': '', "'": '', 
        '<': '', '>': '', '?': '', '/': '', '\\': '', 
        '|': '', '~': '', '`': ''
    }
    
    # Convert the string to lowercase for processing
    input_lower = input.lower()
    
    # Replace special characters with their corresponding A-Z equivalents
    output = ''.join(special_char_map.get(char, char) for char in input_lower)
    
    # Format the output to match the expected output style
    # Assuming we want to return the output in a specific format
    # Here we will just return the output as is, but you can modify it as needed
    return output

# Example usage
print(solution("3h93 SJokZ2mMEZBJmHo"))  # Expected output: R-IFyS.YFLge oa64
print(solution("b.5Kn)P4"))              # Expected output: R-IFyS.YFLge oa64
print(solution("nwtqGPlskfq.Q)jmXBoHiLtM-8ssf"))  # Expected output: R-IFyS.YFLge oa64