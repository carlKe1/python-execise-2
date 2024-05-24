# You are given a file namelist.txt that contains a bunch of names. Some of the names are
# a first name and a last name separated by spaces, like George Washington, while others have
# a middle name, like John Quincy Adams. There are no names consisting of just one word or
# more than three words. Write a program that asks the user to enter initials, like GW or JQA,
# and prints all the names that match those initials. Note that initials like JA should match both
# John Adams and John Quincy Adams.

initials = input("Enter initials: ")
with open("namelist.txt", "r") as file:
    names = file.readlines()

for name in names:
    first, last = name.strip().split()
    if first[0] + last[0] == initials:
        print(name.strip())
