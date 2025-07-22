n = int(input())

for i in range(n):
   
    start = (i + 1) * n
    for j in range(n):
        print(start - j, end=" ")
    print()
