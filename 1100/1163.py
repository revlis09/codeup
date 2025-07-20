a, b, c=map(int,input().split())
total=a+b+c
d=(total//100)%10
if total[1]%2==0:
  print("대박")
else:
  print("그럭저럭")
