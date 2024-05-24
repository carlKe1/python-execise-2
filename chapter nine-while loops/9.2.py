# A good program will make sure that the data its users enter is valid. Write a program that
# asks the user for a weight and converts it from kilograms to pounds. Whenever the user
# enters a weight below 0, the program should tell them that their entry is invalid and then ask
# them again to enter a weight. [Hint: Use a while loop, not an if statement].

def kg_to_pounds(weight_kg):
    # Convert kilograms to pounds
    return weight_kg * 2.20462

def main():
    while True:
        # Ask the user to enter a weight in kilograms
        weight_kg = float(input("Enter weight in kilograms: "))

        if weight_kg < 0:
            # If weight is negative, prompt the user to enter a valid weight
            print("Invalid entry. Weight must be greater than or equal to 0. Please try again.")
        else:
            # If weight is valid, convert it to pounds and print the result
            weight_pounds = kg_to_pounds(weight_kg)
            print(f"{weight_kg} kilograms is equal to {weight_pounds:.2f} pounds.")
            break

if __name__ == "__main__":
    main()
