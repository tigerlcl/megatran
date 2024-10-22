def solution(input):
    # Create a mapping of DNA bases to their partners
    base_pairing = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    
    # Generate the partner sequence
    output = ''.join(base_pairing[base] for base in input)
    
    return output