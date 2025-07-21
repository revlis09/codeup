n=int(input())
sum=0
a=list(map(int, input().split()))
for i in a:
  if i%2!=0:
    sum+=1
print(sum)