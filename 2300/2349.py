n, m = map(int, input().split())

a = []
for _ in range(n):
    b = list(map(int, input().split()))
    a.append(b)

c = 0

for i in range(n - m + 1):  
    for j in range(n - m + 1): 
        total = 0
        for x in range(m):
            for y in range(m):
                total += a[i + x][j + y]
        if total > c:
            c = total
print(c)
