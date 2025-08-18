n, m = map(int, input().split())

a = []
for _ in range(n):
    num = list(map(int, input().split()))
    b = num[1:]
    a.append(b)

c = [0, 1000, 1000, 2000, 3000, 3000, 6000, 6000]

count = [0]*8
for friend in a:
    for t in friend:
        count[t] += 1

total = 0
for i in range(1, 8):
    if count[i] >= m:
        total += c[i] * n

print(total)
