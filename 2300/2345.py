n=int(input())
m=int(input())
a=list(map(int, input().split()))
T=n-m
last=T
count=1
for i in a:
  if T-i>0:
    last=T-i
    count+=1
    continue
if last !=0:
  print(-1)
else:
  print(count)