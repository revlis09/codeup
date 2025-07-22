word = input().split()
n = 0

for w in word:
    n += len(w)


if len(word) > 1:
    n += len(word) - 1

print(n)
