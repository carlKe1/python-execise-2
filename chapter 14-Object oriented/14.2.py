#  Write a class called Product. The class should have fields called name, amount, and price,
# holding the product’s name, the number of items of that product in stock, and the regular
# price of the product. There should be a method get_price that receives the number of
# items to be bought and returns a the cost of buying that many items, where the regular price
# is charged for orders of less than 10 items, a 10% discount is applied for orders of between
# 10 and 99 items, and a 20% discount is applied for orders of 100 or more items. There should
# also be a method called make_purchase that receives the number of items to be bought and
# decreases amount by that much.

class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, quantity):
        if quantity < 10:
            return self.price * quantity
        elif 10 <= quantity < 100:
            return self.price * quantity * 0.9
        else:
            return self.price * quantity * 0.8

    def make_purchase(self, quantity):
        if quantity <= self.amount:
            self.amount -= quantity
            return True
        else:
            return False

# Example usage
product = Product("Widget", 100, 10.0)
print(product.get_price(5))  # Output: 50.0
print(product.get_price(10))  # Output: 90.0
print(product.get_price(100))  # Output: 800.0
product.make_purchase(10)
print(product.amount)  # Output: 90
