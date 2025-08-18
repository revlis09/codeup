a = [
    [6, 7, 3, 2, 0, 5],
    [3, 10, 3, 0, 5, 7],
    [2, 1, 13, 2, 1, 5],
    [6, 11, 0, 4, 8, 4],
    [0, 7, 7, 0, 1, 15],
    [6, 1, 6, 0, 2, 5]
]

max = 0

for i in range(6 - 3 + 1):
    for j in range(6 - 3 + 1):
        total = 0
        for x in range(3):
            for y in range(3):
                total += a[i + x][j + y]
        if total > max:
            max = total

print(max)
