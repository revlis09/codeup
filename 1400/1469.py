n = int(input())

for i in range(1, n+1):
    if i % 2:
        for j in range(i*n, i*n-n, -1):
            print(j, end=' ')
    else:
        for j in range(i*n-n+1, i*n+1):
            print(j, end=' ')
    print()