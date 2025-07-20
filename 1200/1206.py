a, b=map(int, input().split())
if a>b:
  if a%b==0:
    x=a//b
    print(f"{b}*{x}={a}")
  else:
    print("none")
else:
  if b%a==0:
    x=b//a
    print(f"{a}*{x}={b}")
  else:
    print("none")