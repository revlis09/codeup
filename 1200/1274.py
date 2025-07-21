n=int(input())
x="prime"

if n==2:
  x="prime"

for i in range(2, n):
  if n%i==0:
    x="not prime"

print(x)