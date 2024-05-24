# (a) Write a function called add_excitement that takes a list of strings and adds an exclamation point (!) to the end of each string in the list. The program should modify the
# original list and not return anything.

def add_excitement(lst):
    for i in range(len(lst)):
        lst[i] += "!"

# Example usage
strings = ["Hello", "World"]
add_excitement(strings)
print(strings)  # Output: ['Hello!', 'World!']
