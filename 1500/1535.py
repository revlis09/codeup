n=int(input())
a=list(map(int,input().split()))
def num():
  max=0
  for i in range(0, len(a)):
    if a[i]>a[max]:
      max=i
  print(max+1)

num()