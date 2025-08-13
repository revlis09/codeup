def zero(k):
    return k == 0

def plus(k):
    return k > 0

n = int(input())

if zero(n):
    print("zero")
elif plus(n):
    print("plus")
else:
    print("minus")