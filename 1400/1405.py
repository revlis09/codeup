n=int(input())
a=list(map(int, input().split()))
for i in range(n):
  r=a[i:]+a[:i]
  print(*r)
