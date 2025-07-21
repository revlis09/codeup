a, b=map(int,input().split())
money=0
if a%2==0:
  money+=a//2*10
else:
  money+=a//2+1

if b%2==0:
  money+=b//2*10
else:
  money+=b//2+1

print(money)

