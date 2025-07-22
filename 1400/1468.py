n = int(input())

num = 1
for i in range(n):
    if i%2==0:
      for j in range(n):
          print(num, end=" ")
          num += 1
    else:
      num += n - 1  
      for j in range(n):
        print(num - j, end=" ")
      num += 1  
           
    print()
