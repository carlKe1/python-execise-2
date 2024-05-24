# Write a function called first_diff that is given two strings and returns the first location in
# which the strings differ. If the strings are identical, it should return -1

def first_diff(str1, str2):
    for i in range(min(len(str1), len(str2))):
        if str1[i] != str2[i]:
            return i
    if len(str1) != len(str2):
        return min(len(str1), len(str2))
    return -1

# Example usage
print(first_diff("hello", "hallo"))  # Output: 1
print(first_diff("hello", "hello"))  # Output: -1
