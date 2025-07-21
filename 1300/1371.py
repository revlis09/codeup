n=int(input())
space=0
for i in range(n-1, -1, -1):
  print(" "*i+"*"+" "*space+"*")
  space+=2
for j in range(0, n):
  print(" "*j+"*"+" "*(space-2)+"*")
  space-=2