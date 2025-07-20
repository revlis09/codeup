n=int(input())
first=n//10
second=n%10


last=(second*10+first)*2
if last>=100:
  last=last-100
  print(last)
else:
  print(last)
if last>50:
  print("OH MY GOD")
else:
  print("GOOD")
