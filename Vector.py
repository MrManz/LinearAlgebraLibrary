import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def addition(self, v):
        # Better: Use list comprehension
        values = []
        if self.dimension != v.dimension:
            return
        for i in range (0,self.dimension):
            values.append(self.coordinates[i] + v.coordinates[i])
        return Vector(values)

    def substraction(self, v):
        values = []
        if self.dimension != v.dimension:
            return
        for i in range (0,self.dimension):
            values.append(self.coordinates[i] - v.coordinates[i])
        return Vector(values)

    def multiplyScalar(self, scalar):
        values = []
        for i in range(0, self.dimension):
            values.append(self.coordinates[i] * scalar)
        return Vector(values)

    def getMagnitude(self):
        value = 0
        for i in range(0, self.dimension):
            value += self.coordinates[i] ** 2
        return math.sqrt(value)

    def normalize(self):
        return self.multiplyScalar(1 / self.getMagnitude())

    def dotProduct(self, v):
        value = 0
        for i in range(0, self.dimension):
            value += self.coordinates[i] * v.coordinates[i]
        return value

    def angle(self, v):
        return math.acos(self.dotProduct(v) / (self.getMagnitude() * v.getMagnitude()))

v1 = Vector([7.887 , 4.138])
v2 = Vector([-8.802 , 6.776])

v3 = Vector([-5.955 , -4.904, -1.874])
v4 = Vector([-4.496, -8.755, 7.103])

v5 = Vector([3.183 , -7.627])
v6 = Vector([-2.668, 5.319])

v7 = Vector([7.35 , 0.221, 5.188])
v8 = Vector([2.751, 8.259, 3.985])

print(math.degrees(v7.angle((v8))))