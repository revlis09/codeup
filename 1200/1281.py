a, b=map(int, input().split())
sum=0
n=[]
for i in range(a, b+1):
  if i%2==0:
    sum-=i
    n.append(-i)
  else:
    if i==a:
      sum+=i
      n.append(i)
    else:
      sum+=i
      n.append(f"+{i}")
total=0
for i in n:
  if total==0:
    print(i, end="")
print(f"={sum}")
  