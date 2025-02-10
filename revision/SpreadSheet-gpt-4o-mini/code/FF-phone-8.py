def solution(input):
    # Split the input string by spaces and then by dashes to isolate the phone number part
    parts = input.split()
    phone_number = parts[-1]  # Get the last part which contains the phone number
    last_three_digits = phone_number.split('-')[-1]  # Split by dash and get the last segment
    return last_three_digits