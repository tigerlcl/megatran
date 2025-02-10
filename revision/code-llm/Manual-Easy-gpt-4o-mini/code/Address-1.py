def solution(input):
    # Split the input string by commas and take the last part
    parts = input.split(',')
    # The last part contains the state and zip code
    state_zip = parts[-1].strip()
    # Split the state and zip code by space and take the last part (zip code)
    zip_code = state_zip.split()[-1]
    return zip_code