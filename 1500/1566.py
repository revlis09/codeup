def f():
  a, b=map(int, input().split())
  total=1
  for i in range(1, b-1):
    total*=a
  return total

print(f())