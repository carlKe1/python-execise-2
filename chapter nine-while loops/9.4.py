# Write a program that allows the user to enter any number of test scores. The user indicates
# they are done by entering in a negative number. Print how many of the scores are A’s (90 or
# above). Also print out the average.

def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def main():
    scores = []
    total_scores = 0
    num_scores = 0
    num_a_scores = 0
    
    # Input loop
    while True:
        score = float(input("Enter a test score (-1 to finish): "))
        
        # Check if the user wants to finish entering scores
        if score == -1:
            break
        
        # Increment the number of scores and add the score to the list
        num_scores += 1
        total_scores += score
        scores.append(score)
        
        # Check if the score is an A
        if score >= 90:
            num_a_scores += 1
    
    # Calculate average
    if num_scores > 0:
        average = total_scores / num_scores
    else:
        average = 0
    
    # Print results
    print("Number of A's:", num_a_scores)
    print("Average score:", average)

if __name__ == "__main__":
    main()
