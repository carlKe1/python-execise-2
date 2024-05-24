# People often forget closing parentheses when entering formulas. Write a program that asks
# the user to enter a formula and prints out whether the formula has the same number of opening and closing parenthe
# s

# Ask the user to enter a formula
formula = input("Enter a formula: ")

# Count the number of opening and closing parentheses
num_opening_parentheses = formula.count('(')
num_closing_parentheses = formula.count(')')

# Check if the number of opening and closing parentheses are equal
if num_opening_parentheses == num_closing_parentheses:
    print("The formula has the same number of opening and closing parentheses.")
else:
    print("The formula does not have the same number of opening and closing parentheses.")
