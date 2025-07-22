a, b = map(int, input().split())
ax = list(map(int, input().split()))
count = 0
ax.sort()
for i in ax:
  print(i, end=" ")
  count += 1
  if count == b:
    print()
    count = 0  
