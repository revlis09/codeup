a, b, d=input().split()
a=int(a)
b=int(b)
if d=="L":
  for i in range(0, a):
    print(" "*i+"*"*b)
elif d=="R":
  for i in range(a-1, -1, -1):
    print(" "*i+"*"*b)