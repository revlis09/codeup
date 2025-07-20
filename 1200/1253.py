a, b=map(int, input().split())
lot=max(a, b)
low=min(a, b)

for i in range(low, lot+1):
  print(i, end=" ")
