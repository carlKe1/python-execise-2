#  Write a class called Wordplay. It should have a field that holds a list of words. The user
# of the class should pass the list of words they want to use to the class. There should be the
# following methods:
# • words_with_length(length) — returns a list of all the words of length length
# • starts_with(s) — returns a list of all the words that start with s
# • ends_with(s) — returns a list of all the words that end with s
# • palindromes() — returns a list of all the palindromes in the list
# • only(L) — returns a list of the words that contain only those letters in L
# • avoids(L) — returns a list of the words that contain none of the letters in L


class Wordplay:
    def __init__(self, words):
        self.words = words

    def words_with_length(self, length):
        return [word for word in self.words if len(word) == length]

    def starts_with(self, s):
        return [word for word in self.words if word.startswith(s)]

    def ends_with(self, s):
        return [word for word in self.words if word.endswith(s)]

    def palindromes(self):
        return [word for word in self.words if word == word[::-1]]

    def only(self, L):
        return [word for word in self.words if all(letter in L for letter in word)]

    def avoids(self, L):
        return [word for word in self.words if all(letter not in L for letter in word)]

# Example usage
word_list = ["hello", "world", "level", "test", "deed", "python", "noon"]
wp = Wordplay(word_list)
print(wp.words_with_length(5))  # Output: ["hello", "world"]
print(wp.starts_with("l"))  # Output: ["level"]
print(wp.ends_with("d"))  # Output: ["world"]
print(wp.palindromes())  # Output: ["level", "deed", "noon"]
print(wp.only("loe"))  # Output: ["level"]
print(wp.avoids("aeiou"))  # Output: ["python"]
