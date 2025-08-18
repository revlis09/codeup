def f(n):
    num = 0  
    while n > 0:
        digit = n % 10
        num = num * 10 + digit
        n //= 10
    return num

a=int(input())
s = f(a)
print(s)  

