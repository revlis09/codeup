n=int(input())
b=[]
num=[]
for x in range(1, n+1):
   num.append(x)
for i in range(n-1):
  a=int(input())
  b.append(a)
  b.sort()
for j in num:
    if j not in b:
      print(j)