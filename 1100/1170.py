a, b, c=map(int, input().split())
if b<10:
  if c>=100:
    print(f"{a}0{b}{c}")
  else:
    if c>=10:
      print(f"{a}0{b}0{c}")
    else:
      print(f"{a}0{b}00{c}")
elif b>=10 and c>=100:
  print(f"{a}{b}{c}")
else:
  if c>=100:
    print(f"{a}0{b}{c}")
  else:
    if c>=10:
      print(f"{a}{b}0{c}")
    else:
      print(f"{a}{b}00{c}")
    
  