# Write a program that estimates the average number of drawings it takes before the user’s
# numbers are picked in a lottery that consists of correctly picking six different numbers that
# are between 1 and 10. To do this, run a loop 1000 times that randomly generates a set of
# user numbers and simulates drawings until the user’s numbers are drawn. Find the average
# number of drawings needed over the 1000 times the loop runs.

import random

def lottery_draw():
    # Generate six unique random numbers between 1 and 10
    return random.sample(range(1, 11), 6)

def simulate_lottery(user_numbers):
    # Simulate drawings until the user's numbers are drawn
    num_drawings = 0
    while True:
        num_drawings += 1
        drawn_numbers = lottery_draw()
        if set(user_numbers) == set(drawn_numbers):
            return num_drawings

def main():
    # Number of iterations to run the simulation
    iterations = 1000

    # User's numbers
    user_numbers = [int(input(f"Enter number {i + 1} (between 1 and 10): ")) for i in range(6)]

    # Run the simulation
    total_drawings = 0
    for _ in range(iterations):
        total_drawings += simulate_lottery(user_numbers)

    # Calculate the average number of drawings needed
    average_drawings = total_drawings / iterations

    # Print the result
    print("Average number of drawings needed:", average_drawings)

if __name__ == "__main__":
    main()
