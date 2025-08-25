n = int(input())
s = list(map(int, input().split()))
a, b = map(int, input().split())

target = sum(s[a-1:b])

c = 0
cur = 0
d = {}

for x in s:
    cur += x
    if cur == target:
        c += 1
    if cur - target in d:
        c += d[cur - target]
    if cur in d:
        d[cur] += 1
    else:
        d[cur] = 1

print(c)