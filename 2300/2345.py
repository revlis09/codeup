n = []

for i in range(12):
    for j in range(60):
        a = i * 30 + j* 0.5
        b = j* 6

        if a > b:
            c = a - b
        else:
            c = b - a

        if c == 22:
            n.append(f"{i:02d}:{j:02d}")

print(len(n))
for t in n:
    print(t)
