def solution(input):
    # Convert the input string to a float to handle the conversion
    pounds = float(input)
    # Conversion factor from pounds to kilograms
    conversion_factor = 0.45359237
    # Convert pounds to kilograms
    kilograms = pounds * conversion_factor
    # Truncate the result to two decimal places
    truncated_kilograms = int(kilograms * 100) / 100
    # Format the result to two decimal places
    output = f"{truncated_kilograms:.2f}"
    return output