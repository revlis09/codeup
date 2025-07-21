n=int(input())
sum=0
for i in range(1, n+1):
  second=i%10
  if second==1:
    sum+=1
print(sum)