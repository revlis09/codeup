n = int(input())
n_1 = int(input())
target = n - n_1  

count = 0

count += target // 500
target = target % 500

count += target // 100
target = target % 100

count += target // 50
target = target % 50

count += target // 10
target = target % 10

print(count)
