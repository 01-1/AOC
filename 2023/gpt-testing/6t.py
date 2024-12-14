def ways_to_beat_record(time, distance):
    ways = 0
    for hold_time in range(time):
        boat_speed = hold_time
        remaining_time = time - hold_time
        total_distance = boat_speed * remaining_time
        if total_distance > distance:
            ways += 1
    return ways

def calculate_product_of_ways(file_path):
    races = []
    with open(file_path, 'r') as file:
        time_line = next(file)  # Assume the first line contains time values
        distance_line = next(file)  # Assume the second line contains distance values

        # Extract time and distance values
        times = [int(val) for val in time_line.strip().split() if val.isdigit()]
        distances = [int(val) for val in distance_line.strip().split() if val.isdigit()]

        # Calculate the number of ways for each race
        for time, distance in zip(times, distances):
            ways_for_race = ways_to_beat_record(time, distance)
            races.append(ways_for_race)

    # Calculate the product of the number of ways for all races
    result = 1
    for ways in races:
        result *= ways

    return result

# Example file path
file_path = 'path/to/your/race_data.txt'

# Calculate the product of the number of ways for each race from the file
result = calculate_product_of_ways(file_path)

# Print the result
print("The product of the number of ways for each race is:", result)
