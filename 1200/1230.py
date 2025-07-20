a=list(map(int, input().split()))
for i in a:
  if i<=170:
    print("CRASH", i)
    break
else:
   print("PASS")