n, a, b = map(int, input().split())
x = list(map(int, input().split()))  
y = list(map(int, input().split()))  

c = 0  
d = 0  

for i in range(1, n + 1):
    if i not in x and i not in y:
        c += 1
    if i in x and i in y:
        d += 1

print(c, d)

