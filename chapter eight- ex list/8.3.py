# Write a simple quote-of-the-day program. The program should contain a list of quotes, and
# when the user runs the program, a randomly selected quote should be printed.

import random

def print_quote(quotes):
    # Select a random quote from the list
    random_quote = random.choice(quotes)
    print("Quote of the day:")
    print(random_quote)

def main():
    # List of quotes
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln"
    ]

    # Print a random quote
    print_quote(quotes)

if __name__ == "__main__":
    main()
