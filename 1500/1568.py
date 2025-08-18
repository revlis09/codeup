def f():
    n = int(input()) 
    arr = list(map(int, input().split()))
    c, d = map(int, input().split())  
    a = arr[c-1:d]
    max=0
    for i in range(1,len(a)):
        if a[max]<a[i]:
            max=i

    return max

print(f())