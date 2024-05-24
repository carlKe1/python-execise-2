# For this problem, use the dictionary from the beginning of this chapter whose keys are month
# names and whose values are the number of days in the corresponding months.
# (b) Print out all of the keys in alphabetical order.
# (c) Print out all of the months with 31 days.
# (d) Print out the (key-value) pairs sorted by the number of days in each mont
# (e) Modify the program from part (a) and the dictionary so that the user does not have to
# know how to spell the month name exactly. That is, all they have to do is spell the first
# three letters of the month name correctly.

def month_operations(months):
    # (a) Ask the user to enter a month name and tell them how many days are in the month
    month_name = input("Enter a month name: ")
    if month_name.capitalize() in months:
        print("There are {} days in {}.".format(months[month_name.capitalize()], month_name))
    else:
        print("Month '{}' not found.".format(month_name))

    # (b) Print out all keys (month names) in alphabetical order
    print("Month names in alphabetical order:")
    for month in sorted(months.keys()):
        print(month)

    # (c) Print out all months with 31 days
    print("Months with 31 days:")
    for month, days in months.items():
        if days == 31:
            print(month)

    # (d) Print out the (key-value) pairs sorted by the number of days in each month
    print("Months sorted by the number of days:")
    sorted_months = sorted(months.items(), key=lambda x: x[1])
    for month, days in sorted_months:
        print("{} - {} days".format(month, days))

def main():
    months = {
        'January': 31, 'February': 28, 'March': 31,
        'April': 30, 'May': 31, 'June': 30,
        'July': 31, 'August': 31, 'September': 30,
        'October': 31, 'November': 30, 'December': 31
    }
    month_operations(months)

if __name__ == "__main__":
    main()
