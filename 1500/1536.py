

n=int(input())
a=list(map(int,input().split()))
def num():
  min=a[0]
  for i in range(0, len(a)):
    if a[i]<min:
      min=a[i]
  print(min)

num()