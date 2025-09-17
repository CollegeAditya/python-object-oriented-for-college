from math import sqrt
from math import pow

a, b = input("enter values a, b for the first point: ").split()
c, d = input("enter values a, b for the second point: ").split()

distance = sqrt((pow(int(a)-int(c), 2) + pow(int(b)-int(d), 2)))

print(distance)