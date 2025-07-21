n=int(input())
sum=0
a=list(map(int, input().split()))
for i in a:
  if i%5==0:
    sum+=i
print(sum)
