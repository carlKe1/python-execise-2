# Write a program that uses a dictionary that contains ten user names and passwords. The
# program should ask the user to enter their username and password. If the username is not in
# the dictionary, the program should indicate that the person is not a valid user of the system. If
# the username is in the dictionary, but the user does not enter the right password, the program
# should say that the password is invalid. If the password is correct, then the program should
# tell the user that they are now logged in to the system.

def user_authentication(users):
    username = input("Enter your username: ")
    if username in users:
        password = input("Enter your password: ")
        if users[username] == password:
            print("You are now logged in to the system.")
        else:
            print("Invalid password.")
    else:
        print("Invalid username.")

def main():
    users = {
        'user1': 'password1',
        'user2': 'password2',
        'user3': 'password3',
        'user4': 'password4',
        'user5': 'password5'
    }
    user_authentication(users)

if __name__ == "__main__":
    main()
