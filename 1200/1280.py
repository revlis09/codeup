a, b=map(int, input().split())
sum=0
n=[]
for i in range(a, b+1):
  if i%2==0:
    sum-=i
    n.append(-i)
  else:
    sum+=i
    n.append(f"+{i}")
for i in n:
  print(i, end="")
print(f"={sum}")