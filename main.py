from triangle import Triangle

t1 = Triangle()         #default constructor
print("triangle 1:", t1)

t2 = Triangle(5.5)      #equilateral triangle
print("triangle 2:",t2)

t3= Triangle (2.2,3.6)      #isoscales triangle
print("triangle 3:",t3)

t4 = Triangle (1.1,2.2,3.3)     #scalene triangle
print("triangle 4:",t4)

t5 = Triangle (t4)      #copy constructor
print("triangle 5:",t5)

t6 = Triangle(3,4,5)
print(t6.is_right_angled())