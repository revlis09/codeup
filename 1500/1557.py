def f(n):
    total = 0
    for i in range(1, n + 1):
        for j in range(1, n+1):
          if i*j==num:
             total+=1
    return total

num=int(input())
print(f(num))