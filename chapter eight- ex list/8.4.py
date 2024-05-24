# Write a simple lottery drawing program. The lottery drawing should consist of six different
# numbers between 1 and 48.

import random

def lottery_draw():
    # Generate six unique random numbers between 1 and 48
    lottery_numbers = random.sample(range(1, 49), 6)
    return sorted(lottery_numbers)

def main():
    # Perform the lottery drawing
    winning_numbers = lottery_draw()

    # Print the winning numbers
    print("Lottery Drawing Results:")
    print("Winning Numbers:", winning_numbers)

if __name__ == "__main__":
    main()
