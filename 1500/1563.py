def f():
    a, b, c = map(int, input().split())
  
    if (b <= a <= c) or (c <= a <= b):
        return a
  
    elif (a <= b <= c) or (c <= b <= a):
        return b
    
    else:
        return c

print(f())
