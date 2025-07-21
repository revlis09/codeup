a, b=map(int, input().split())
for i in range(a, b+1):
  for j in range(1, 10):
    print(f"{i}*{j}={i*j}")