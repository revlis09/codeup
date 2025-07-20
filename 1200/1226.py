a=list(map(int, input().split()))
b=list(map(int, input().split()))
count=0
x=a[:6]
plus=a[6]
for i in b:
  if i in x:
      count+=1
if count==6:
  print(1)
elif count==5 and plus in b:
  print(2)
elif count==5:
  print(3)
elif count==4:
  print(4)
elif count==3:
  print(5)
else:
  print(0)