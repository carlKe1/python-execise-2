# Write a program that asks the user to enter a word that contains the letter a. The program
# should then print the following two lines: On the first line should be the part of the string up
# to and including the first a, and on the second line should be the rest of the string. Sample
# output is shown below:
# Enter a word: buffalo
# buffa
# lo

# Ask the user to enter a word containing the letter 'a'
word = input("Enter a word containing the letter 'a': ")

# Find the index of the first occurrence of 'a'
index_of_a = word.find('a')

# Print the substring before and after the first 'a'
print(word[:index_of_a+1])
print(word[index_of_a+1:])
