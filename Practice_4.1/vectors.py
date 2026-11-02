import math


class Vector:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __mul__(self, k):
        return Vector(self.x * k, self.y * k, self.z * k)

    def __rmul__(self, k):
        return self.__mul__(k)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def normalized(self):
        length = abs(self)
        if length == 0:
            raise ValueError("Нулевой вектор нельзя нормализовать")
        return Vector(self.x / length, self.y / length, self.z / length)

    def angle(self, other):
        if abs(self) == 0 or abs(other) == 0:
            raise ValueError("Нельзя найти угол с нулевым вектором")
        cos_a = self.dot(other) / (abs(self) * abs(other))
        if cos_a > 1:
            cos_a = 1
        if cos_a < -1:
            cos_a = -1
        return math.acos(cos_a)

    def is_orthogonal(self, other):
        return abs(self.dot(other)) < 1e-9

    def is_collinear(self, other):
        cross = self.cross(other)
        return abs(cross.x) < 1e-9 and abs(cross.y) < 1e-9 and abs(cross.z) < 1e-9


def triangle_area(a, b, c):
    v1 = b - a
    v2 = c - a
    return 0.5 * abs(v1.cross(v2))


def volume(a, b, c):
    return abs(a.dot(b.cross(c)))
