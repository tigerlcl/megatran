def solution(input):
    # Split the input string by the '-' character
    parts = input.split('-')
    # The last part contains the last three digits of the phone number
    last_three_digits = parts[-1]
    return last_three_digits