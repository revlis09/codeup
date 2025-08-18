n = int(input())
n_1 = int(input())
target = n - n_1
a, b, c = map(int, input().split())

traps = sorted([a, b, c], reverse=True)

count = 0

for t in traps:
    count += target // t
    target = target % t

if target != 0:
    print(-1)
else:
    print(count)
