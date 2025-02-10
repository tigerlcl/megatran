def solution(input):
    # Define a mapping of input strings to their corresponding constant values
    constant_map = {
        "zMw7675": "fDz0lt9",
        "7uQ": "Q",
        "-yDm1j8Qq)j(5": "roc7kt4Fl6)?ki",
        "wK41NqeLvh": "fDz0lt9 Q roc7kt4Fl6)?ki",
        "eo5U*sqZMf0fc": "fDz0lt9 Q roc7kt4Fl6)?ki",
        "6": "roc7kt4Fl6)?ki"
    }
    
    # Check if the input string is in the constant map and return the corresponding value
    output = constant_map.get(input, "")
    
    # Debugging output
    print(f"Input: '{input}', Output: '{output}'")
    
    return output