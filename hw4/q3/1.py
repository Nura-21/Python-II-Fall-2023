import math

# Function to calculate the coordinates of the clock hands
def calculate_clock_coordinates(time):
    # Split the time into hours and minutes
    hours, minutes = map(int, time.split(':'))

    # Calculate the angles for both hands
    minute_angle = (360 / 60) * minutes
    hour_angle = (360 / 12) * (hours % 12) + (30 / 60) * minutes  # Adjust for minutes

    # Calculate the coordinates for the hour hand
    hour_x = 10 + 6 * math.cos(math.radians(90 - hour_angle))
    hour_y = 10 - 6 * math.sin(math.radians(90 - hour_angle))

    # Calculate the coordinates for the minute hand
    minute_x = 10 + 9 * math.cos(math.radians(90 - minute_angle))
    minute_y = 10 - 9 * math.sin(math.radians(90 - minute_angle))

    return hour_x, hour_y, minute_x, minute_y

# Read the number of test cases
num_test_cases = int(input())

# Process each test case
for _ in range(num_test_cases):
    time = input()
    hour_x, hour_y, minute_x, minute_y = calculate_clock_coordinates(time)
    print(f"{hour_x:.2f} {hour_y:.2f} {minute_x:.2f} {minute_y:.2f}")
