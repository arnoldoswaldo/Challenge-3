class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def compute_length(self):
        dx = self.end_point.x - self.start_point.x
        dy = self.end_point.y - self.start_point.y
        return (dx ** 2 + dy ** 2) ** 0.5

    def compute_slope(self):
        dx = self.end_point.x - self.start_point.x
        dy = self.end_point.y - self.start_point.y
        if dx == 0:
            return float('inf')
        else:
            return dy / dx

    def compute_horizontal_cross(self):
        return self.start_point.y == 0 or self.end_point.y == 0

    def compute_vertical_cross(self):
        return self.start_point.x == 0 or self.end_point.x == 0

class Rectangle:
    def __init__(self, top_line, right_line, bottom_line, left_line):
        self.top_line = top_line
        self.right_line = right_line
        self.bottom_line = bottom_line
        self.left_line = left_line

    def area(self):
        return self.top_line.compute_length() * self.right_line.compute_length()

    


p1 = Point(2, 0) 
p2 = Point(6, 4)
line1 = Line(p1, p2)
print("Longitud de la línea:", line1.compute_length())
print("Pendiente de la línea:", line1.compute_slope())
print("Intersección horizontal:", line1.compute_horizontal_cross())
print("Intersección vertical:", line1.compute_vertical_cross())

rectangle = Rectangle(line1, line1, line1, line1)
print("Área del rectángulo:", rectangle.area())

