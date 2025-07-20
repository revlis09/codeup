n=int(input())
year=2012-n+1
if year>=2000:
  last=year-2000
  print(last, 3)
else:
  last=year-1900
  print(last, 1)