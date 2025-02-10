def solution(input):
    # Split the input string into sections based on spaces
    sections = input.split(' ')
    
    # Reverse the character order of each section
    reversed_sections = [section[::-1] for section in sections]
    
    # Reverse the order of the sections
    reversed_sections.reverse()
    
    # Join the reversed sections back together with spaces
    output = ' '.join(reversed_sections)
    
    return output