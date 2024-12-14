
def sum_calibration_values_from_file(file_path):
    total_sum = 0

    with open(file_path, 'r') as file:
        for line in file:
            # Find the first and last digits in each line
            first_digit = next((char for char in line if char.isdigit()), None)
            last_digit = next((char for char in reversed(line) if char.isdigit()), None)

            # Check if both digits are found
            if first_digit is not None and last_digit is not None:
                calibration_value = int(first_digit + last_digit)
                total_sum += calibration_value

    return total_sum

# Example file path
file_path = 'path/to/your/calibration_file.txt'
file_path = 'aocold/1'

# Calculate the sum of all calibration values from the file
result = sum_calibration_values_from_file(file_path)

# Print the result
print("The sum of all calibration values is:", result)
