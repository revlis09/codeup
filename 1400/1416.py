n = int(input())
b = []

if n == 0:
    print(0)
else:
    while n > 0:
        num = n % 2
        b.append(num)
        n = n // 2

    for i in range(len(b)-1, -1, -1):
        print(b[i], end="")
