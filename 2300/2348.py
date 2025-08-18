
n = int(input())

a = []
for _ in range(n):
    b = list(map(int, input().split()))
    a.append(b)

c = 0

for i in range(n - 2 + 1):  
    for j in range(n - 2 + 1): 
        total = 0
        for x in range(2):
            for y in range(2):
                total += a[i + x][j + y]
        if total > c:
            c = total
print(c)
