def solution(input):
    # Split the input string into a list of words (first and last name)
    names = input.split()
    # Reverse the order of the names
    reversed_names = ' '.join(names[::-1])
    # Return the reversed names
    return reversed_names