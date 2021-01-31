a_km = int(input("How many kilometers did you run on the first day? "))
b_km = int(input("How many kilometers you'd like to run? "))
day = 0

while a_km < b_km:
    a_km *= 1.1
    day += 1
    if a_km >= b_km:
        print(f"You'll achieve your goal on day {day} if you run 10% more every day!")
