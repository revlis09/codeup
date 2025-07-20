age, gender=input().split()
month=int(age[:2])
gender=int(gender)
if gender==2 or gender==1:
  print(2012-(1900+month)+1)
else:
  print(2012-(2000+month)+1)

