class Rectangle:
    def __init__(self, length, breadth,cost=0):
        self.length = length
        self.breadth = breadth
        self.cost = cost

    def set(self):
        i = input("Enter the value")
        self.length = i

    def get_perimeter(self):
        return 2 * (self.length + self.breadth)

    def get_area(self):
        return self.length * self.breadth

    def calculate_cost(self):
        area = self.get_area()
        return area * self.cost


# breadth = 120 cm, length = 160 cm, 1 cm^2 = Rs 2000
r = Rectangle(160, 120, 2000)
print("Area of Rectangle is"+" "+str(r.get_area())+" "+"cm^2")
print("Cost of rectangular field is"+" "+"RS"+" "+str(r.calculate_cost()))
