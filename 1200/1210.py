
kal=0

a=list(map(int, input().split()))
for i in a:
  if i==1: 
    kal+=400
  elif i==2:
    kal+=340
  elif i==3:
    kal+=170
  elif i==4:
    kal+=100
  else:
    kal+=70

if kal>500:
  print("angry")
else:
  print("no angry")