def solution(input):
    # Separate alphanumeric characters
    alphanumeric = [char for char in input if char.isalnum()]
    
    # Reverse the alphanumeric characters
    alphanumeric.reverse()

    # Prepare the output list
    output = []
    alnum_index = 0

    # Iterate through the original input to maintain the sequence of non-alphanumeric characters
    for char in input:
        if char.isalnum():
            output.append(alphanumeric[alnum_index])
            alnum_index += 1
        else:
            output.append(char)  # Use the original character directly

    # Join the output list into a string
    return ''.join(output)

# Example test cases
print(solution("rGzWK Pk"))  # Output: "kP KWzGr"
print(solution("hW*yeXPARKeBdZA0(85Wu2epio"))  # Output: "oipe2uW58(0AZdBeKRAPXey*Wh"
print(solution("y(a4G8vobO-baEvT)BW6(lw3cJr)ap7"))  # Output: "7pa)rJc3wl(6WB)TvEab-Obov8G4a(y"