"""import math

AB = int(input())
BC = int(input())

r = str(int(round(math.degrees(math.atan2(AB, BC)))))

print(r + '°')"""

"""import math

ab = float(input())
bc = float(input())

h = math.sqrt(ab**2+bc**2)
h = h/2.0
adj = bc/2.0

print(str(int(round(math.degrees(math.acos(adj/h)))))+"°")"""

import math

AB, BC = int(input()), int(input())
hype = math.hypot(AB, BC)  # to calculate hypotenuse
res = round(math.degrees(math.acos(BC / hype)))  # to calculate required angle
degree = chr(176)  # for DEGREE symbol
print(res, degree, sep='')
