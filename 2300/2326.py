n = int(input())
s = list(map(int, input().split()))
a, b = map(int, input().split())

target = sum(s[a-1:b])

c = 0
cur = 0
w = {}

for x in s:
    cur += x
    if cur == target:
        c += 1
    if cur - target in w:
        c += w[cur - target]
    if cur in w:
        w[cur] += 1
    else:
        w[cur] = 1

print()