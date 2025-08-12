n=int(input())
def num():
  a=0
  for i in range(1, n-1):
    if i*i==n:
      a=i
      print(i)
  if a==0:
    print(n)
  
num()