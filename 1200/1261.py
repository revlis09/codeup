a=list(map(int,input().split()))
corect=0
for i in a:
  if i%5==0:
    print(i)
    corect=1
    break
if corect==0:
  print(0)