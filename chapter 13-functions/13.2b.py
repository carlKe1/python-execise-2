# (b) Write the same function except that it should not modify the original list and should
# instead return a new list.
def add_excitement(lst):
    new_lst = []
    for string in lst:
        new_lst.append(string + "!")
    return new_lst

# Example usage
strings = ["Hello", "World"]
new_strings = add_excitement(strings)
print(new_strings)  # Output: ['Hello!', 'World!']
