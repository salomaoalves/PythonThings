import math

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

x = (x2-x1)**2
y = (y2-y1)**2
new = x + y
dist = math.sqrt(new)

if dist >= 10:
    print("longe")
else:
    print("perto")
