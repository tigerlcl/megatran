def solution(input):
    # Convert input string to uppercase
    input = input.upper()
    
    # Replace special characters with their equivalents
    replacements = {
        '.': '1',
        '-': '2',
        ' ': '3',
        '(': '4',
        ')': '5',
        '&': '6',
        '@': '7',
        '#': '8',
        '$': '9',
        '%': '0'
    }
    
    for key, value in replacements.items():
        input = input.replace(key, value)
    
    return input