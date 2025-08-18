n=int(input())
a=[10, 5, 3, 1]
count=0
for i in a:
  b=n//i
  n=n%i
  count+=b
if n==0:
  print(count)