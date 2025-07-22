a, b = map(int, input().split())

num = 1
total = a * b

for i in range(a):
    start = total - (i + 1) * b + 1
    for j in range(b):
        print(start + j, end=" ")
    print()