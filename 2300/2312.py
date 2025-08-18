a, b, c = map(int, input().split())
n = list(map(int, input().split()))
n_1 = list(map(int, input().split()))

count = 0      
count_1 = 0    

for x, y in zip(n, n_1):
    if x == y:
        count += 1

for i in range(1, a + 1):
    if i not in n and i not in n_1:
        count_1 += 1

print(count, count_1)

