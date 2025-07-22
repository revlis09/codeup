num = list(map(int, input().split()))
num.sort()
for x in range(2):
    print(num[x], end=" ")