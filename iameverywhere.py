def count_unique_cities():
    test_cases = int(input())  # Read the number of test cases

    for _ in range(test_cases):
        cities_visited = int(input())  # Read the number of cities visited
        city_set = set()  # Create an empty set to store unique cities

        for _ in range(cities_visited):
            city = input().strip()  # Read the city name and remove leading/trailing whitespace
            city_set.add(city)  # Add the city to the set

        unique_cities = len(city_set)  # Count the number of unique cities
        print(unique_cities)  # Print the result


# Run the function to test the example input
count_unique_cities()
