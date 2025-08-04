import math
class Triangle:
    _object_count=0
    def __init__(self, a=1.0, b=1.0, c=1.0):
        # copy constructor
        if isinstance (a, Triangle):
            self._a = a.a
            self._b = a.b
            self._c = a.c
        # equilateral triangle (all sides same)
        elif b == 1.0 and c == 1.0:
            self._a = self._b = self._c = a

        # isosceles triangle (2 sides same)
        elif c==1.0:
            self._a = self._b = a
            self._c= b

        # scalene triangle (all sides diff)
        else:
            self._a = a
            self._b = b
            self._c = c

        Triangle._object_count += 1

    @classmethod
    def object_count(cls):
        return cls._object_count

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, value):
        if value > 0:
            self._a = value

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, value):
        if value > 0:
            self._b = value

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        if value > 0:
            self._c = value

    def perimeter(self):
        return self.a + self.b + self.c
    
    def is_right_angled(self):
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2)
    
    def __str__(self):
        return (f"Triangle with sides a={self.a}, b={self.b}, c={self.c}\n"
                f"Perimeter: {self.perimeter()}, "
                f"Right-angled: {self.is_right_angled()}")
    
    def show (self):
        print (f"sides: {self.a}, {self.b}, {self.c}")




