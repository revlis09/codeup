a, b=map(int, input().split())
count=0
while count<b:
  for i in range(0, a):
    print(" "*i+"*")
  for j in range(a-2, -1, -1):
    print(" "*j+"*")
  count+=1