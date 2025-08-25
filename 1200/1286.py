b=[]
for _ in range(5):
  n=int(input())
  b.append(n)
max=0
min=0
for i in range(len(b)):
  if b[max]<b[i]:
    max=i
  elif b[min]>b[i]:
    min=i
print(b[max])
print(b[min])