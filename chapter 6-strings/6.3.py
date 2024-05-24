# At a certain school, student email addresses end with @student.college.edu, while professor email addresses end with @prof.college.edu. Write a program that first asks the
# user how many email addresses they will be entering, and then has the user enter those addresses. After all the email addresses are entered, the program should print out a message
# indicating either that all the addresses are student addresses or that there were some professor addresses entered

# Ask the user how many email addresses they will be entering
num_addresses = int(input("How many email addresses will you be entering? "))

# Initialize counters for student and professor addresses
student_count = 0
professor_count = 0

# Ask the user to enter the email addresses
for i in range(num_addresses):
    email = input(f"Enter email address {i + 1}: ")
    if email.endswith("@student.college.edu"):
        student_count += 1
    elif email.endswith("@prof.college.edu"):
        professor_count += 1

# Print the result based on the counts
if student_count == num_addresses:
    print("All addresses are student addresses.")
elif professor_count == num_addresses:
    print("All addresses are professor addresses.")
else:
    print("There were some professor addresses entered.")
