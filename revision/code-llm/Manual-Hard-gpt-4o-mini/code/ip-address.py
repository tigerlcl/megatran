def solution(input):
    # Split the input IP address into its octets
    octets = input.split('.')
    
    # Convert each octet to hexadecimal and format it
    hex_parts = [format(int(octet), '02x') for octet in octets]
    
    # Join the last two octets to form the final output
    output = '::' + ''.join(hex_parts[-2:]) + ':' + hex_parts[-1]
    
    return output