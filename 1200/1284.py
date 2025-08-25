n = int(input())

a=1
for i in range(2, n):
    if n % i == 0:       
        j = n // i
        if i%2!=0 or j!=0:      
          print(i, j)
          a=0
          break            
if a==1:
  print("wrong number")