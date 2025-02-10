def solution(input):
    # Split the input string by dots to get the individual octets
    octets = input.split('.')
    
    # Convert each octet to its hexadecimal representation
    hex_octets = [format(int(octet), '02x') for octet in octets]
    
    # Combine the hexadecimal octets into a single string
    hex_string = ''.join(hex_octets)
    
    # Format the final IPv6 address
    output = f"::{hex_string[:4]}:{hex_string[4:]}"
    
    return output