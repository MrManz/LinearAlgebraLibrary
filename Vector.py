import math
from decimal import Decimal, getcontext

getcontext().pred = 30

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(Decimal(x) for x in coordinates)
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
            values.append(self.coordinates[i] * Decimal(scalar))
        return Vector(values)

    def getMagnitude(self):
        value = 0
        for i in range(0, self.dimension):
            value += self.coordinates[i] ** 2
        return Decimal(math.sqrt(value))

    def normalize(self):
        return self.multiplyScalar(Decimal(1.0) / self.getMagnitude())

    def dotProduct(self, v):
        value = Decimal(0.0)
        for i in range(0, self.dimension):
            value += self.coordinates[i] * v.coordinates[i]
        return value

    def angle(self, v):
        return math.acos(self.dotProduct(v) / (self.getMagnitude() * v.getMagnitude()))

    def checkIfParallel(self, v):
        return(self.isZero() or v.isZero()
                or self.angle(v) == 0
                or self.angle(v) == math.pi )

    def checkIfOrt(self, v):
        tolerance = 1e-10
        if abs(self.dotProduct(v)) < tolerance:
            return True
        else:
            return False

    def isZero(self):
        return self.getMagnitude() < 1e-10

    def getProjection(self, v):
        unitVector = v.normalize()
        return (unitVector.multiplyScalar(self.dotProduct(unitVector)))


v1 = Vector([3.039 , 1.879])
v2 = Vector([ 0.825 , 2.036])

print(v1.getProjection(v2))
