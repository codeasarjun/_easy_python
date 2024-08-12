
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(2, 3)
p2 = Point(4, 5)

print(p1)  # Uses __repr__
print(p2)

p3 = p1 + p2  # Uses __add__
print(p3)

print(p1 == p2)  # Uses __eq__
