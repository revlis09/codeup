x1, y1 = map(int, input().split())
a= int(input())
x2, y2 = map(int, input().split())

c = (x2 - x1)**2 + (y2 - y1)**2
b = a**2

if c < b:
  d = "in"
elif c == b:
  d = "on"
else:
  d = "out"

print(d)