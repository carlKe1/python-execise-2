# Modify the higher/lower program so that when there is only one guess left, it says 1 guess,
# not 1 guesses

def guess_number():
    import random
    number = random.randint(1, 100)
    guesses = 0

    while True:
        guess = int(input("Guess the number (between 1 and 100): "))
        guesses += 1

        if guess < number:
            print("Higher!")
        elif guess > number:
            print("Lower!")
        else:
            if guesses == 1:
                print("Congratulations! You guessed the number in 1 guess!")
            else:
                print(f"Congratulations! You guessed the number in {guesses} guesses!")
            break

def main():
    print("Welcome to the Higher/Lower game!")
    print("I'm thinking of a number between 1 and 100.")
    guess_number()

if __name__ == "__main__":
    main()
