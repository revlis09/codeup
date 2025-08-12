n=int(input())
def num():
  a=1
  for i in range(2, n):
    if n%i==0:
      a=0
      break
  if a==1:
    print("prime")
  else:
    print("composite")

num()