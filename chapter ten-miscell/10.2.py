# Write a program that asks the user to enter a word. Rearrange all the letters of the word
# in alphabetical order and print out the resulting word. For example, abracadabra should
# become aaaaabbcdrr

def rearrange_letters(word):
    sorted_word = ''.join(sorted(word))
    return sorted_word

def main():
    word = input("Enter a word: ")
    rearranged_word = rearrange_letters(word)
    print("Rearranged word:", rearranged_word)

if __name__ == "__main__":
    main()
