def solution(input):
    parts = input.split()
    if len(parts) == 3:
        parts[2] = parts[2][:-1] + parts[0][-1]
    return ' '.join(parts)