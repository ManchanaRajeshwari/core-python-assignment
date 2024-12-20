def calculate_fare(trips):
    base_fare = 50
    distance_fare = 10
    total_cost = 0
    for trip in trips:
        cost = base_fare + (trip * distance_fare)
        total_cost += cost
        print(f"Trip distance {trip} km :${cost}")
    return total_cost
trips = list(map(int, input("Enter trips with space-separated distances: ").split()))
print(f"Total Fare: ${calculate_fare(trips)}")
