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

v1 = Vector([-0.221 , 7.437])
v2 = Vector([8.813 , -1.331, -6.247])
v3 = Vector([5.581 , -2.136])
v4 = Vector([1.996 , 3.108, -4.554])

print(v4.normalize())