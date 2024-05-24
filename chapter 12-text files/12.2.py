# You are given a file called grades.txt, where each line of the file contains a one-word student username and three test scores separated by spaces, like below:.
# GWashington 83 77 54
# JAdams 86 69 90
# Write code that scans through the file and determines how many students passed all three
# tests.

with open("grades.txt", "r") as file:
    lines = file.readlines()

pass_count = 0
for line in lines:
    username, score1, score2, score3 = line.strip().split()
    if int(score1) >= 60 and int(score2) >= 60 and int(score3) >= 60:
        pass_count += 1

print("Number of students passing all three tests:", pass_count)
