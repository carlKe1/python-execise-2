# Write a program that repeatedly asks the user to enter product names and prices. Store all
# of these in a dictionary whose keys are the product names and whose values are the prices.
# When the user is done entering products and prices, allow them to repeatedly enter a product
# name and print the corresponding price or a message if the product is not in the dictionary.

def create_product_dictionary():
    products = {}
    while True:
        product_name = input("Enter product name (or 'done' to finish): ")
        if product_name.lower() == 'done':
            break
        price = float(input("Enter price for {}: $".format(product_name)))
        products[product_name] = price
    return products

def print_product_price(products):
    while True:
        product_name = input("Enter a product name to get its price (or 'done' to exit): ")
        if product_name.lower() == 'done':
            break
        if product_name in products:
            print("Price of {} is ${}".format(product_name, products[product_name]))
        else:
            print("Product '{}' not found.".format(product_name))

def main():
    print("Enter product names and prices:")
    products = create_product_dictionary()
    print("Products:", products)
    print("\nEnter a product name to get its price:")
    print_product_price(products)

if __name__ == "__main__":
    main()

