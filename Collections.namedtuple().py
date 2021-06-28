"""from collections import namedtuple

Point = namedtuple('Point', 'x y')
pt1 = Point(1, 2)
pt2 = Point(3, 4)

dot_product = (pt1.x * pt2.x) + (pt1.y * pt2.y)
print(dot_product)

Car = namedtuple('Car', 'Price Mileage Colour Class')
xyz = Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
print(type(xyz))

print(xyz.Class)"""

from collections import namedtuple

N = int(input())
row = input().split()

total = 0

for i in range(0, N):
    students = namedtuple('student', row)
    r1, r2, r3, r4 = input().split()
    student = students(r1, r2, r3, r4)
    total += int(student.MARKS)

print('{:.2f}'.format(total/N))