n=int(input())
if n==1 or n==2 or n==3 or n%10==1 or n%10==2 or n%10==3:
  if n==11 or n==12 or n==13:
    print(f"{n}th")
  else:
    if n==1 or n%10==1:
      print(f"{n}st")
    elif n==2 or n%10==2:
      print(f"{n}nd")
    else:
      print(f"{n}rd")
else:
  print(f"{n}th")