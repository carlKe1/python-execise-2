# Write a program that takes any two lists L and M of the same size and adds their elements
# together to form a new list N whose elements are sums of the corresponding elements in L
# and M. For instance, if L=[3,1,4] and M=[1,5,9], then N should equal [4,6,13]

# Function to add corresponding elements of two lists
def add_lists(L, M):
    # Initialize an empty list to store the sums
    N = []
    # Iterate through the lists and add corresponding elements
    for i in range(len(L)):
        N.append(L[i] + M[i])
    return N

# Example lists
L = [3, 1, 4]
M = [1, 5, 9]

# Call the function to add the lists
N = add_lists(L, M)

# Print the resulting list
print("The resulting list after adding L and M:", N)
