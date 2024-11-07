def analyze_car_movement():
    # Read the input as three space-separated integers
    input_str = input().strip()
    positions = list(map(int, input_str.split()))
    x1, x2, x3 = positions

    # Calculate the distances traveled in the first and second intervals
    first_interval = x2 - x1
    second_interval = x3 - x2

    # Determine the movement pattern
    if (first_interval > 0 and second_interval < 0) or (first_interval < 0 and second_interval > 0):
        result = "turned"
    elif abs(second_interval) > abs(first_interval):
        result = "accelerated"
    elif abs(second_interval) < abs(first_interval):
        result = "braked"
    else:
        result = "cruised"

    # Output the result
    print(result)

# Call the function to execute
analyze_car_movement()
