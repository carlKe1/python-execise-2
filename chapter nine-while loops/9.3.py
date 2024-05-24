# Write a program that asks the user to enter a password. If the user enters the right password,
# the program should tell them they are logged in to the system. Otherwise, the program
# should ask them to reenter the password. The user should only get five tries to enter the
# password, after which point the program should tell them that they are kicked off of the
# system

def login():
    # Correct password
    correct_password = "password123"
    
    # Number of tries allowed
    max_tries = 5
    
    # Attempt counter
    tries = 0
    
    while tries < max_tries:
        # Ask the user to enter the password
        password = input("Enter the password: ")
        
        # Check if the entered password is correct
        if password == correct_password:
            print("Logged in successfully!")
            return True
        else:
            tries += 1
            remaining_tries = max_tries - tries
            if remaining_tries > 0:
                print(f"Incorrect password. You have {remaining_tries} tries left.")
            else:
                print("Sorry, you've reached the maximum number of tries. Access denied.")
                return False

def main():
    login()

if __name__ == "__main__":
    main()
