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


v1 = Vector([8.218 , -9.341])
v2 = Vector([-1.129 , 2.111])

print(v1.addition(v2))

v3 = Vector([7.119 , 8.215])
v4 = Vector([-8.223 , 0.878])

print(v3.substraction(v4))

v5 = Vector([1.671 , -1.012, -0.318])
print(v5.multiplyScalar(7.41))