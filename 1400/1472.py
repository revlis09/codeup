a, b=map(int, input().split())

for j in range(a):
  count=0
  if j % 2 == 0:
    for i in range(a*b-b+1, a*b+1):
      print(i, end=" ")
      end=i
    print()
  else:
    for i in range(a*b-b, -1, -1):
      if count==b:
        break
      else:
        count+=1
        print(i, end=" ")
    print()
  