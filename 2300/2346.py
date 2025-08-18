n = []
num=int(input())

for i in range(12):
    for j in range(60):
        a = i * 60 + j
        b = j* 12

        if a > b:
            c = a - b
        else:
            c = b - a

        if c == num:
            n.append(f"{i:02d}:{j:02d}")

print(len(n))
for t in n:
    print(t)
