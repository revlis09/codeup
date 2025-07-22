n = int(input())
count=0
while count<n:
  for i in range(1, n + 1):
    if i % 2 != 0:
        spaces = (n - i) // 2
        stars = i
        print(" " * spaces + "*" * stars+" " * spaces)
        

        
