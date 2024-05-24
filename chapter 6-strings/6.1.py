# A simple way to estimate the number of words in a string is to count the number of spaces
# in the string. Write a program that asks the user for a string and returns an estimate of how
# many words are in the string.

# Ask the user for a string
user_string = input("Enter a string: ")

# Count the number of spaces in the string
number_of_spaces = user_string.count(' ')

# Estimate the number of words by adding 1 to the number of spaces
# (as each word is separated by a space)
number_of_words = number_of_spaces + 1

# Print the estimate of the number of words in the string
print("Estimated number of words:", number_of_words)
