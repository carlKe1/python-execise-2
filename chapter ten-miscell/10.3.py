# Write a program that takes a list of ten prices and ten products, applies an 11% discount to
# each of the prices displays the output like below, right-justified and nicely formatted.
# Apples $ 2.45
# Oranges $ 18.02
# ...
# Pears $120.03

def apply_discount(prices):
    discounted_prices = [price * 0.89 for price in prices]
    return discounted_prices

def main():
    products = ["Apples", "Oranges", "Pears", "Bananas", "Grapes", "Mangoes", "Pineapples", "Strawberries", "Blueberries", "Watermelons"]
    prices = [2.45, 18.02, 120.03, 0.99, 5.75, 8.50, 3.25, 4.99, 6.75, 10.50]

    discounted_prices = apply_discount(prices)

    for product, price in zip(products, discounted_prices):
        print(f"{product:12} ${price:7.2f}")

if __name__ == "__main__":
    main()
