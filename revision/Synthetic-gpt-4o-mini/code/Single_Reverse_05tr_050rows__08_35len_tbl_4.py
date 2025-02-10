def solution(input):
    # Split the input by periods
    segments = input.split('.')
    # Reverse the order of segments and then reverse each segment
    reversed_segments = [segment[::-1] for segment in reversed(segments)]
    # Join the reversed segments with periods
    output = '.'.join(reversed_segments)
    return output