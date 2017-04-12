#!/usr/bin/env python
# -*- coding: utf8 -*-

import collections
import math


# class Vector(VectorBase):
class Vector(collections.namedtuple('VectorBase', 'x, y')):
    def __init__(self, x, y):
        super(Vector, self).__init__()

    def __repr__(self):
        return 'Vector({x!r}, {y!r})'.format(x=self.x, y=self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, v):
        return Vector(self.x + v.x, self.y + v.y)

    def __mul__(self, scalar):
        return Vector(scalar*self.x, scalar*self.y)

    def __rmul__(self, scalar):
        return Vector(scalar*self.x, scalar*self.y)


if __name__ == '__main__':
    v0 = Vector(2, 3)
    v1 = Vector(4, 1)
    print(v0)
    print(v1)
    print(abs(v0))
    print(bool(v0))
    print(v1 + v0)
    print(v1*10)
    print(10*v1)

