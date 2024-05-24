# When playing games where you have to roll two dice, it is nice to know the odds of each
# roll. For instance, the odds of rolling a 12 are about 3%, and the odds of rolling a 7 are about
# 17%. You can compute these mathematically, but if you don’t know the math, you can write
# a program to do it. To do this, your program should simulate rolling two dice about 10,000
# times and compute and print out the percentage of rolls that come out to be 2, 3, 4, . . . , 12

import random

def roll_two_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def compute_percentage_of_rolls(num_rolls):
    rolls_count = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        total = roll_two_dice()
        rolls_count[total] += 1

    total_rolls = sum(rolls_count.values())
    percentages = {total: (count / total_rolls) * 100 for total, count in rolls_count.items()}
    return percentages

def main():
    num_rolls = 10000
    percentages = compute_percentage_of_rolls(num_rolls)

    print("Total   Percentage")
    for total, percentage in percentages.items():
        print(f"{total}: {percentage:.2f}%")

if __name__ == "__main__":
    main()
