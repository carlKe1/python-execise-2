#  Write a program that asks the user for a weight in kilograms. The program should convert
# the weight to kilograms, formatting the result to one decimal place

def kg_to_pounds(weight_kg):
    # Convert kilograms to pounds
    return weight_kg * 2.20462

def main():
    # Ask the user to enter a weight in kilograms
    weight_kg = float(input("Enter weight in kilograms: "))
    
    # Convert kilograms to pounds
    weight_pounds = kg_to_pounds(weight_kg)
    
    # Format the result to one decimal place
    formatted_weight_pounds = "{:.1f}".format(weight_pounds)
    
    # Print the result
    print(f"{weight_kg:.1f} kilograms is equal to {formatted_weight_pounds} pounds.")

if __name__ == "__main__":
    main()
