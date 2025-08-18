def f(n, m):
  a = set()
  for i in range(1, int(m**0.5) + 1):
    if m % i == 0:
      a.add(i)
      a.add(m // i)
  
  b = set()
  for i in range(1, n // m + 1):
    b.add(m * i)
    
  result = a.union(b)
  
  return len(result)

n = 997
m = 36

answer = f(n, m)
print(answer)