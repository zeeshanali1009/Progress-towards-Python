# This program calcualtes the square , cube and square root of the number

class Calculator:
    def __init__(self, number):
        self.number = number

    def Square(self):
        print(f"Square of the number is: {self.number ** 2}")

    def Cube(self):
        print(f"Cube of the number is: {self.number ** 3}")

    def Squareroot(self):
        print(f"Square root of the number is: {self.number ** 0.5}")


object_01 = Calculator(9)


object_01.Square()
object_01.Cube()
object_01.Squareroot()
