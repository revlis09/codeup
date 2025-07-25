n=int(input())
sum=0
for i in range(n):
  print(sum, end=" ")
  for j in range(n):
    if sum==n*n:
      break
    else:
      sum+=1
     
  print()