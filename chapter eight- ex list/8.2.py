# Write a program that allows the user to enter five numbers (read as strings). Create a string
# that consists of the user’s numbers separated by plus signs. For instance, if the user enters 2,
# 5, 11, 33, and 55, then the string should be '2+5+11+33+55'.

def main():
    # Prompt the user to enter five numbers
    numbers = []
    for i in range(5):
        num_str = input(f"Enter number {i + 1}: ")
        numbers.append(num_str)

    # Create a string consisting of the user's numbers separated by plus signs
    result = '+'.join(numbers)

    # Print the resulting string
    print("Resulting string:", result)

if __name__ == "__main__":
    main()
