n=int(input())
s = list(map(int, input().split()))
a, b=map(int, input().split())

target = sum(s[a:b])  

c = 0
cur = 0
d = {0: 1}  

for x in s:
    cur += x
    c += d.get(cur - target, 0)
    d[cur] = d.get(cur, 0) + 1

print(c)
