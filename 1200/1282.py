a=int(input())
b=0
c=0
for i in range(1,a+1):
    b=i*i
    if b >a:
        b =(i-1)*(i-1)
        b=a-b
        c=i-1
        break
print(b, c)