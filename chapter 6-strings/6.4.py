# Write a program that asks the user to enter a string, then prints out each letter of the string
# doubled and on a separate line. For instance, if the user entered HEY, the output would be
# HH
# EE
# YY

# Ask the user to enter a string
user_string = input("Enter a string: ")

# Print each letter of the string doubled and on a separate line
for char in user_string:
    print(char * 2)
