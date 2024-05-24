# . Write a function called rectangle that takes two integers m and n as arguments and prints
# out an m × n box consisting of asterisks. Shown below is the output of rectangle(2,4)
# ****
# ****

def rectangle(m, n):
    for _ in range(m):
        print('*' * n)

# Example usage
rectangle(2, 4)
