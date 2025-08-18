a, b = input().split()

results = []

for i in a:
    for j in b:
        c = i + j
        if c not in results:
            results.append(c)

seen = []
for r in results:
    if r[0] == r[1]:
        if r[0] == "A":
            d = "A"
        elif r[0] == "B":
            d = "B"
        elif r[0] == "O":
            d = "O"
    elif ("A" in r and "B" in r):
        d = "AB"
    elif ("A" in r and "O" in r):
        d = "A"
    elif ("B" in r and "O" in r):
        d = "B"
    
    if d not in seen:
        seen.append(d)

for d in sorted(seen):
    print(d, end=" ")
