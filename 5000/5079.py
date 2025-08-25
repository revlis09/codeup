n=int(input())
c=input()
a=0, b=0
for i in range(n):
  if c[i]=="A":
    a+=1
  else:
    b+=1
if a>b:
  print("A")
else:
  print("B")