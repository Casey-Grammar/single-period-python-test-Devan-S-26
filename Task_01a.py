# Task 01a - Calculate Total
# Write a function called calculate_total(price, quantity)
# that returns the total cost.
#
# Example:
# calculate_total(4.5, 3) -> 13.5

def calculate_total(price, quantity):
        # Write your code here
        if price < 0 or quantity < 0:
            raise ValueError("Please input a number that ISNT negative.")
        return price * quantity

def main(): 
    try:
          price = float(input("Enter price: "))
          quantity = int(input("Enter quantity: "))
          total = calculate_total(price, quantity)
          print(total)
    except ValueError as v:
          print(f'Invalid input: {v}')