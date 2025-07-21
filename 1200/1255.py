a, b=map(float,input().split())
while True:
  if a<=b:
    print("%0.2f" %a, end=" ")
    a=a+0.01
  else:
    break
