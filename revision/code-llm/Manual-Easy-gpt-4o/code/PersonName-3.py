def solution(input):
    # Split the input string by tabs
    parts = input.split('\t')
    # Format the output string as "LastName, FirstName MiddleInitial."
    output = f"{parts[0]}, {parts[2]} {parts[1]}."
    return output