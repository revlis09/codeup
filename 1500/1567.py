def f():
    n = int(input()) 
    arr = list(map(int, input().split()))
    c, d = map(int, input().split())  
    total = sum(arr[c-1:d])  
    return total

print(f())
