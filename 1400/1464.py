a, b = map(int, input().split())

num = a * b  

for i in range(a):
    for j in range(b):  
        print(num, end=" ")
        num -= 1
    print()
