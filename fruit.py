"""
A module for demonstrating the Meta class
"""

from time import sleep
class AppleBasket:
    """
    A class representing a basket of apples.
    """

    def __init__(self, color, quantity):
        self.apple_color = color
        self.apple_quantity = quantity

    def increase(self):
        self.apple_quantity += 1

    def __str__(self):
        sleep(1)
        return "A basket of {} {} apples.".format(self.apple_quantity, self.apple_color)


example1 = AppleBasket("red", 4)
example2 = AppleBasket("blue", 50)

print("Example1:", example1, "\nExample2:", example2)
