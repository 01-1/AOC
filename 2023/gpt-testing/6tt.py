def ways_to_beat_record(total_time, distance):
    ways = 0
    for hold_time in range(1, total_time):  # Start from 1 to avoid holding for the entire duration
        boat_speed = hold_time
        remaining_time = total_time - hold_time
        total_distance = boat_speed * remaining_time
        if total_distance > distance:
            ways += 1
    return ways

# Given values for the longer race
total_time = 59707878

record_distance = 430121812131276

# Calculate the number of ways to beat the record
ways_to_win = ways_to_beat_record(total_time, record_distance)

# Print the result
print("The number of ways to beat the record is:", ways_to_win)
