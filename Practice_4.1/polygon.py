import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Polygon:
    def __init__(self, points):
        if len(points) < 3:
            raise ValueError("Нужно минимум 3 вершины")
        self._points = []
        for p in points:
            self._points.append(Point(p.x, p.y))

    def __len__(self):
        return len(self._points)

    def perimeter(self):
        total = 0.0
        n = len(self._points)
        for i in range(n):
            p1 = self._points[i]
            p2 = self._points[(i + 1) % n]
            total = total + math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)
        return total

    def area(self):
        n = len(self._points)
        s = 0.0
        for i in range(n):
            p1 = self._points[i]
            p2 = self._points[(i + 1) % n]
            s = s + p1.x * p2.y - p2.x * p1.y
        return abs(s) / 2.0

    def move(self, dx, dy):
        for p in self._points:
            p.x = p.x + dx
            p.y = p.y + dy

    def bounding_box(self):
        xs = []
        ys = []
        for p in self._points:
            xs.append(p.x)
            ys.append(p.y)
        return (min(xs), min(ys), max(xs), max(ys))

    def is_convex(self):
        n = len(self._points)
        sign = 0
        for i in range(n):
            p0 = self._points[i]
            p1 = self._points[(i + 1) % n]
            p2 = self._points[(i + 2) % n]
            cross = (p1.x - p0.x) * (p2.y - p1.y) - (p1.y - p0.y) * (p2.x - p1.x)
            if cross != 0:
                if sign == 0:
                    if cross > 0:
                        sign = 1
                    else:
                        sign = -1
                elif (cross > 0 and sign < 0) or (cross < 0 and sign > 0):
                    return False
        return True

    def __lt__(self, other):
        return self.area() < other.area()
