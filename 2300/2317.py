m = int(input())
berries = list(map(int, input().split()))
n = int(input())

juice = []
raw = []
pie = []

for berry in berries:
  if berry < n:
    juice.append(berry)
  elif berry > n:
    pie.append(berry)
  else: # berry == n
    raw.append(berry)

result = juice + raw + pie

print(*result)
