# Write a class called Investment with fields called principal and interest. The constructor should set the values of those fields. There should be a method called value_after that
# returns the value of the investment after n years. The formula for this is p(1 + i)
# n
# , where p is
# the principal, and i is the interest rate. It should also use the special method __str__ so that
# printing the object will result in something like below:
# Principal - $1000.00, Interest rate - 5.12%

class Investment:
    def __init__(self, principal, interest):
        self.principal = principal
        self.interest = interest

    def value_after(self, n):
        return self.principal * (1 + self.interest) ** n

    def __str__(self):
        return f"Principal - ${self.principal:.2f}, Interest rate - {self.interest*100:.2f}%"

# Example usage
investment = Investment(1000, 0.0512)
print(investment)  # Output: Principal - $1000.00, Interest rate - 5.12%
print(investment.value_after(5))  # Output: value after 5 years
