# Write a function called sum_digits that is given an integer num and returns the sum of the
# digits of num.

def sum_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

# Example usage
print(sum_digits(45893))  # Output: 29
