# Write a program that asks the user for an integer and creates a list that consists of the factors
# of that integer.

# Function to find factors of an integer
def find_factors(number):
    factors = []
    # Iterate from 1 to the given number
    for i in range(1, number + 1):
        # Check if i is a factor of the given number
        if number % i == 0:
            factors.append(i)
    return factors

# Ask the user for an integer
try:
    user_integer = int(input("Enter an integer: "))
    if user_integer <= 0:
        print("Please enter a positive integer.")
    else:
        # Call the function to find factors of the integer
        factors = find_factors(user_integer)
        print("The factors of", user_integer, "are:", factors)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
