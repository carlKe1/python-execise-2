#  Using the dictionary created in the previous problem, allow the user to enter a dollar amount
# and print out all the products whose price is less than that amount.

def print_products_less_than_amount(products):
    amount = float(input("Enter a dollar amount: $"))
    print("Products with price less than ${}:".format(amount))
    for product, price in products.items():
        if price < amount:
            print("{} - ${}".format(product, price))

def main():
    print("Enter product names and prices:")
    products = create_product_dictionary()
    print("\nEnter a dollar amount to see products with price less than that:")
    print_products_less_than_amount(products)

if __name__ == "__main__":
    main()
