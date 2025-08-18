def f(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total

num=int(input())
print(f(num))