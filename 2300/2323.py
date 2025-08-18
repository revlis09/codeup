n = int(input())
s = list(map(int, input().split()))
a, b = map(int, input().split())

target = sum(s[a:b])

c = 0
cur = 0
d = {0: 1}

for x in s:
    cur += x
    if cur - target in d:
        c += d[cur - target]
    if cur in d:
        d[cur] += 1
    else:
        d[cur] = 1

print(c)

