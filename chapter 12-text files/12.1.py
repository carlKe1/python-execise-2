# You are given a file called class_scores.txt, where each line of the file contains a oneword username and a test score separated by spaces, like below:.
# GWashington 83
# JAdams 86
# Write code that scans through the file, adds 5 points to each test score, and outputs the usernames and new test scores to a new file, scores2.txt.

with open("class_scores.txt", "r") as file:
    lines = file.readlines()

with open("scores2.txt", "w") as new_file:
    for line in lines:
        username, score = line.strip().split()
        new_score = int(score) + 5
        new_file.write(f"{username} {new_score}\n")
