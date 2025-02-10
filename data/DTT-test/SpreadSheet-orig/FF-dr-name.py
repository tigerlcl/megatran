def solution(input):
    # Split the input string to get the first name
    first_name = input.split()[0]
    # Prefix 'Dr.' to the first name
    output = f"Dr. {first_name}"
    return output