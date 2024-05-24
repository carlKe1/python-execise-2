# You are given a file called students.txt. A typical line in the file looks like:
# walter melon melon@email.msmary.edu 555-3141
# There is a name, an email address, and a phone number, each separated by tabs. Write a
# program that reads through the file line-by-line, and for each line, capitalizes the first letter
# of the first and last name and adds the area code 301 to the phone number. Your program
# should write this to a new file called students2.txt. Here is what the first line of the new
# file should look like:
# Walter Melon melon@email.msmary.edu 301-555-3141

initials = input("Enter initials: ")
with open("namelist.txt", "r") as file:
    names = file.readlines()

for name in names:
    first, last = name.strip().split()
    if first[0] + last[0] == initials:
        print(name.strip())
