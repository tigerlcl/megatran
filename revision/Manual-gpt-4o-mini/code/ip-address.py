def solution(input):
    # Split the IPv4 address into its components
    octets = input.split('.')
    
    # Convert each octet to hexadecimal and format it
    hex_parts = [format(int(octet), '02x') if i < 2 else format(int(octet), 'x') for i, octet in enumerate(octets)]
    
    # Combine the first two octets and the last octet into a single hexadecimal representation
    ipv6_address = '::' + ''.join(hex_parts[:2]) + ':' + ''.join(hex_parts[2:])
    
    return ipv6_address