a, b = map(int, input().split())

num = a * b  

for i in range(a):
  current = num - i 
  for j in range(b):
    print(current, end=" ")
    current -= a
  print()