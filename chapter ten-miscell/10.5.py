# Write a program that uses a boolean flag variable in determining whether two lists have any
# items in common.

def lists_have_common_items(list1, list2):
    # Initialize a boolean flag variable
    common_items_found = False

    # Iterate over each item in the first list
    for item1 in list1:
        # Check if the item is present in the second list
        if item1 in list2:
            # If a common item is found, set the flag variable to True and break out of the loop
            common_items_found = True
            break

    # Return the value of the flag variable
    return common_items_found

def main():
    # Example lists
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]

    # Check if the lists have any common items
    if lists_have_common_items(list1, list2):
        print("The lists have common items.")
    else:
        print("The lists do not have any common items.")

if __name__ == "__main__":
    main()
