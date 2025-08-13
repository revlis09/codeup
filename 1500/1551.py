n=int(input())
a=list(map(int, input().split()))
num=int(input())
b=1
for i in range(len(a)):
  if a[i]==num:
    print(i+1)
    b=0
    break
if b==1:
  print(-1)
