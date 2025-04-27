import math

class Vector2D:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def rotation(self):
        return math.degrees(math.atan2(self.y, self.x))

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

v = Vector3D(*map(int, input("Enter x, y, z: ").split()))
print("Magnitude:", v.magnitude(), "Rotation:", v.rotation())
